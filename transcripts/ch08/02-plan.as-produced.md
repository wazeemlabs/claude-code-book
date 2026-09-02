# logsift v1 — project structure and build order

## Context

The repo currently holds only `SPEC.md`, `CLAUDE.md`, a `.gitignore`, and a venv with
the dev tools (pytest 9.1, pytest-cov, hypothesis, ruff, mypy 2.3). No package, no
`pyproject.toml`, no tests. SPEC.md is the binding contract for v1.

The goal of this plan: fix the package skeleton, the plugin protocol, the two built-in
parsers, the filter expression pipeline, aggregation and output — and pin an order in
which each step ends with a full green test suite, per the test-first convention in
CLAUDE.md. No code is written yet.

Two facts shape the whole plan:

1. **Entry points only exist after an install.** `importlib.metadata.entry_points`
   reads `.dist-info`, so `pip install -e .` is step 0, and any change to
   `[project.entry-points."logsift.parsers"]` needs a reinstall to take effect.
   Nothing about parser discovery can be tested before that.
2. **The core never imports a parser.** `clf` and `logfmt` reach the core only through
   the entry point group, so the plugin API is exercised on every run.

---

## Two decisions I need from you

**1. Build backend: setuptools or hatchling?** You asked for setuptools; SPEC.md §2
line 37 says hatchling, and CLAUDE.md makes the spec binding. I plan to follow your
instruction (setuptools) and amend SPEC.md §2 in the same commit so the contract
stays true to the code. Say the word if you'd rather keep hatchling. Neither is
installed, so either way `pip install -e .` will pull the backend from PyPI once.

**2. Is a quoted ISO 8601 literal temporal or string?** SPEC §6.3's table says
"unquoted **or quoted** ISO 8601 timestamp → temporal", but the same section says a
quoted literal selects string mode, and the lexer rule is phrased for unquoted tokens
("begins with four digits followed by `-`"). I plan to resolve it as: a quoted literal
whose content begins with four digits followed by `-` **and** parses as ISO 8601 is
temporal; every other quoted literal is a string. Consequence to accept:
`path == "2026-09-01T00:00:00Z"` can never be a string comparison. The alternative
(quotes always mean string) makes the table row dead text.

A third, smaller call I've made rather than asked: with zero matched records, table
mode prints the header row **and** its `-` separator row. §8.2 says "only the header
is printed"; I read the separator as part of the header block.

---

## Layout

```
pyproject.toml            setuptools backend, dynamic version from logsift.__version__
src/logsift/              (module list exactly as SPEC §12)
tests/
  conftest.py             fake-distribution fixture, log fixtures, console-script locator
  data/                   log fixture files (clf, combined, logfmt, mixed, .gz, binary junk)
  test_*.py               one per module
  test_cli.py             subprocess end-to-end
  test_properties.py      hypothesis
  test_packaging.py       wheel build + fresh-venv install (marked slow)
```

`pyproject.toml` essentials:

- `requires-python = ">=3.10"`, `[build-system] requires = ["setuptools>=64"]`,
  `build-backend = "setuptools.build_meta"`.
- `[tool.setuptools.dynamic] version = {attr = "logsift.__version__"}` — one source of
  truth for `--version`, no second copy in the metadata.
- `[project.scripts] logsift = "logsift.cli:main"`.
- `[project.entry-points."logsift.parsers"]` — `clf` and `logfmt`. **Added at step 6,
  not step 0**: an entry point naming a module that does not exist yet breaks discovery
  for every test that runs before it.
- `[project.optional-dependencies] dev = [pytest, pytest-cov, hypothesis, ruff, mypy,
  build]`. `build` is one beyond SPEC §2's dev list; it exists so the packaging gate
  can run `python -m build --no-isolation` without reaching the network.
- ruff: `target-version = "py310"`, select `E,F,I,UP,B,SIM,RUF`. mypy: `strict = true`
  over `src/` and `tests/` (SPEC §2), which is a superset of CLAUDE.md's documented
  `mypy --strict src/`, so that command stays correct.

---

## The pieces, and the seams that matter

### `record.py`
`Level`, `ParseResult`, `Record` verbatim from SPEC §3. `fields` is wrapped in
`types.MappingProxyType` at construction so a frozen record is actually frozen.
A `Record.parse_error_record(raw, source, lineno, reason)` constructor keeps the
"ts/level/message None, fields empty" invariant in one place instead of at each of the
three call sites in `pipeline.py`.

### `timeparse.py`
- `parse_iso8601(text) -> datetime | None` — hand-written; date, `T` or space
  separator, `HH:MM[:SS[.f{1,9}]]`, offset `Z` / `±HH:MM` / `±HHMM` / `±HH`, none.
  Fractional digits beyond 6 are truncated (microsecond resolution). Returns naive when
  the input carries no offset; never raises.
- `resolve_zone(name) -> ZoneInfo` — raises a typed `UnknownZone` the CLI turns into
  exit 2.
- `local_zone()` — the `--assume-tz` default, from `datetime.now().astimezone().tzinfo`.
  `zoneinfo` cannot reverse-lookup an IANA name, so the stderr notice reports the
  zone's `tzname()` (e.g. `PKT`) when no explicit `--assume-tz` was given.
- `to_utc(dt, assume_tz)` — pure. The *one-time* "assuming timezone X" stderr line is
  emitted by `pipeline.py`, which owns diagnostics; keeping it out of `timeparse` is
  what lets the function be property-tested.
- Ambiguous or nonexistent local times use `fold=0` and are documented, not guessed at.

### `expr/` — the filter language
- **`lexer.py`** — tokens carry their source offset, which is what produces the caret in
  §6.5. Literal typing happens here: unquoted token starting with four digits and `-`
  → timestamp; `true`/`false` → bool; numeric → numeric; bareword matching a `Level`
  name (case-insensitive) → level; quoted → string, unless the decision above applies.
  Any other bareword in literal position is a syntax error.
- **`parser.py`** — recursive descent over SPEC §6.2, frozen-dataclass AST
  (`Or`, `And`, `Not`, `Cmp`). Errors raise `FilterSyntaxError(message, pos, expected)`;
  `cli.py` formats it as the three-line block in §6.5. Regexes for `~` are compiled at
  compile time, so a bad pattern is an expression error before input is read (exit 1).
- **`eval.py`** — the shared value layer, and the main place duplication could creep in:
  - `resolve_field(record, name) -> object | MISSING` — core name wins over `fields`
    per §6.1. **Also used by `agg.py` (`count by FIELD`) and `render.py` (`--columns`).**
    One implementation, three callers.
  - `render_filter_str(value) -> str | None` — the §6.3 string form. **Also the
    group-key function for `count by` (§9 defers to §6.3).** Distinct from display
    rendering, which lives in `render.py` and honours `--tz` and `-` for `None`.
  - `coerce_number(value) -> float | None` — §6.3 numeric rule. **Also used by
    `p50`/`p95`**, so "skipped as non-numeric" means exactly what the filter means.
  - `Kleene` enum plus `k_and` / `k_or` / `k_not`, tested directly against §6.4's
    tables. Explicit enum rather than `bool | None`, so UNKNOWN is never mistaken for
    "no answer yet".
- **`__init__.py`** — `compile(text) -> CompiledFilter`, exposing `.matches(record)`
  (True only for TRUE) and `.field_names`, plus a mutable `.fields_seen` that
  evaluation populates. That set is what feeds the §6.5 "referenced but never present"
  warning without threading extra state through the pipeline.

### `plugin.py`
- `API_VERSION`, the `runtime_checkable` `Parser` protocol. Validation of a loaded
  object is **explicit attribute checks**, not `isinstance` — it gives a message naming
  the missing attribute, and `issubclass` on a data protocol is a TypeError trap.
  The protocol still earns its keep as the static type.
- `LoadedParser(parser, dist, name)` and `discover() -> Registry`. `discover` returns a
  fresh registry each call (no module-level cache) so tests can install fake dists and
  rediscover.
- Skips, each with the stderr warning §4.3/§4.2 requires: import failure, wrong
  `api_version` (naming distribution and both versions), malformed `name`.
- `Registry.resolve(spec)` — bare `NAME` (ambiguous → typed error → exit 2, listing
  every providing distribution) and `DIST:NAME`, always accepted.
- `Registry.sniff_order()` — sorted by `(-priority, dist)`; emits the §4.4 collision
  warning, which says outright that the tie-break is arbitrary.

### `reader.py`
- `open_source(path)` — `-` → stdin, `*.gz` → `gzip` by suffix only, else a plain
  binary open; wrapped in `TextIOWrapper(encoding="utf-8", errors="replace")`.
- **Preflight matters**: §5 requires exit 2 *before any output*, so `cli.py` opens
  every input up front, and for `.gz` reads one byte through the decompressor to force
  the header check. Handles stay open for the run.
- Yields `(lineno, text)` for **every** line including blanks, newline stripped.
  Blank-line counting lives in `pipeline.py`, not here — see the next note.

### `sniff.py`
Buffers `(lineno, line)` pairs until 100 non-empty lines are seen, calls
`can_parse(sample_text)` in registry order with exceptions caught (disqualify + warn,
never abort), and returns the chosen parser chained back in front of the remainder.

The trap this design avoids: if the reader counted blanks, replaying the sample would
double-count them, and if the sample dropped blanks, line numbers would drift. Both are
fixed by having the reader be dumb about blanks and the pipeline count them exactly once.

### `pipeline.py`
The parse loop, plus the `Stats` object that owns every counter and formats the §8.4
stderr summary (keeping `cli.py` well under 450 lines).

- blank → count, skip. `parse` → `None` → parse-error record, reason
  `"parser returned None"`. Raised → parse-error record with `f"{type}: {msg}"`,
  traceback to stderr once per exception type under `-v`.
- Circuit breaker: 100 **consecutive** raises → typed error → exit 2 naming parser and
  distribution. Reset on any line that does not raise.
- Timestamp normalization (aware → UTC; naive → `--assume-tz` → UTC) with the one-time
  "assuming timezone" line on first actual localization.
- §4.5 field-name collision: a `fields` key shadowing a core name warns once per name,
  at first use. The key stays in `fields` (unreachable in the filter namespace, omitted
  from JSON output).

### `agg.py`
`parse_agg_spec(text)` (errors → exit 1) and four aggregators behind
`add(record)` / `result()`. `count by` and `top` sort by `(-count, key)`. Percentiles
buffer into `array.array("d")`, warn past 10M values, print `n/a` at zero values and the
lone value at one (`statistics.quantiles` needs two). Group cardinality warns past 1M.
Group keys and numeric coercion come from `expr.eval` — no second copy of §6.3.

### `render.py`
`TableRenderer` (buffer 100 rows, width = max(header, values) capped at 60, truncate
with a trailing `...`, control characters escaped so one record is one line, `None` →
`-`, `ts` in `--tz` at seconds precision) and `JsonlRenderer` (core keys in §8.2's fixed
order, extras sorted, colliding extras omitted, `separators=(",",":")`,
`ensure_ascii=False`). Aggregation output reuses the same table machinery for the
two-column group table.

### `cli.py`
argparse; `--agg` uses `action="append"` so a second occurrence is a usage error
(exit 2) rather than a silent overwrite. Order of operations is exit-code-driven:
compile filter and agg spec (exit 1) → resolve zones and parser name (exit 2) →
preflight all inputs (exit 2) → stream. Broken pipe is caught at the top level:
stderr to devnull, `os._exit(0)`, no traceback.

---

## Build order

Each step ends with `pytest -q`, `ruff check .`, and `mypy --strict` green. Steps 1–3
and 5 need no install; step 4 onward assume `pip install -e ".[dev]"` has been run.

| # | Step | Ends green on |
| --- | --- | --- |
| 0 | `pyproject.toml` (no entry points yet), `src/logsift/__init__.py` with `__version__`, `__main__.py`, empty `tests/`, tool config. `pip install -e ".[dev]"`. | import + version test |
| 1 | `record.py` | construction, frozen-ness, `Level` ordering, parse-error invariants |
| 2 | `timeparse.py` | offsets, `Z`, 1–9 fractional digits, naive, garbage, and specifically the inputs 3.10's `fromisoformat` rejects; unknown zone |
| 3 | `expr/` — lexer, then parser, then eval, then `compile` | every literal form, precedence, parens, unterminated string, bad regex, caret position; full Kleene tables; every coercion and every UNKNOWN path |
| 4 | `plugin.py` **+ `tests/conftest.py` fake-distribution fixture** | all six SPEC §13 plugin fakes: wrong api_version, name collision, colliding fields, `can_parse` raising, always-raising, intermittently-raising |
| 5 | `parsers/clf.py`, `parsers/logfmt.py` — written against the protocol, unit-tested as plain objects | fixture lines, malformed lines, `bytes` as `-`, the `LC_TIME` locale trap, level aliases, `raw_level`, `ts_raw` |
| 6 | Declare both entry points in `pyproject.toml`, **reinstall** | discovery finds `clf` and `logfmt` through `importlib.metadata`, priorities 50 / 40 |
| 7 | `reader.py` | stdin, file, `.gz`, malformed gzip, missing file, binary bytes → replacement chars, linenos across blanks |
| 8 | `sniff.py` | picks by priority, sample not consumed, linenos survive the replay, `can_parse` raising disqualifies |
| 9 | `pipeline.py` | error isolation, circuit breaker at exactly 100, counters, tz normalization, collision warning fires once |
| 10 | `agg.py` | spec errors, ordering including exact ties, 0/1/2-value percentiles, non-numeric skipped and counted |
| 11 | `render.py` | width sampling under and over 100 rows, 60-char truncation, control escaping, JSON key order, colliding extras omitted |
| 12 | `cli.py` — wiring, summary, exit codes, broken pipe | subprocess end-to-end: every exit code path, `--json` shape, table output, both `--agg` modes, gzip, stdin, multiple inputs of different formats, empty match exiting 0, `\| head -20` exiting quietly |
| 13 | `tests/test_properties.py` + `tests/test_packaging.py` + README | filter evaluation never raises; AST round-trip; De Morgan / double negation / commutativity; `count by` total equals `count`; wheel installs into a fresh venv and discovers both parsers from the installed dist |

The one ordering constraint worth defending: **step 4 before step 5.** Writing the
built-in parsers after the protocol and its fakes means they are written against the
published contract and type-checked against it, rather than the protocol being
back-fitted to whatever the built-ins happened to do.

Commit at each step. The two steps that carry a reinstall (0 and 6) should say so in
the commit message, since a stale `.dist-info` produces a confusing "no parser claimed
the input" failure.

---

## Verification

Per step: `pytest -q`, `ruff check . && ruff format --check .`, `mypy --strict src/ tests/`.

End to end, once step 13 lands:

```
pytest -q --cov=logsift                       # full suite incl. hypothesis
python -m build --no-isolation                # wheel
pip install --force-reinstall dist/*.whl      # into a throwaway venv
logsift tests/data/access.log --filter 'status >= 500' --agg 'top 10 path'
logsift tests/data/app.log --filter 'level >= WARN and message ~ "timeout"' --json
logsift tests/data/access.log.gz --agg 'p95 bytes'
cat tests/data/app.log | logsift --parser logfmt --columns ts,level,service,message
logsift tests/data/big.log | head -20; echo $?    # must be 0, no traceback
```

The packaging test asserts the installed run discovers both parsers from the wheel's
metadata and not from the source tree — that is the check that the plugin architecture
is real rather than an import in disguise.

Note: the local venv is Python 3.14, so the suite never exercises 3.10's stricter
`fromisoformat`. That is fine, because `parse_iso8601` is ours on every version and its
tests pin the behaviour directly — but CI should run the matrix from 3.10 up.
