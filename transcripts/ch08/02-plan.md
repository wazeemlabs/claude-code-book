## Prompt

```
@SPEC.md @CLAUDE.md
Plan the project structure: src layout, pyproject.toml
with setuptools, the console script entry point, the
parser plugin protocol, the two built-in parsers, the
filter expression parser, aggregation, and output.
Propose the order to build it in so that each step has
a passing test suite. Do not write code yet.
```

## Session


[tool: Bash {"command": "ls -la && echo \"--- tree ---\" && find . -not -path './.git/*' -not -name '.git' | head -50 && echo \"--- settings ---\" && cat .claude/settings.json && echo \"--- gitignore ---\" && cat .gitignore 2>/dev/null | head -30 && echo \"--- python ---\" && python3 --version", "description": ]
[result: total 80
drwxr-xr-x@  8 reader  staff    256 Sep  2 13:21 .
drwxr-xr-x@  6 reader  staff    192 Sep  2 13:07 ..
drwxr-xr-x@  3 reader  staff     96 Sep  2 13:21 .claude
drwxr-xr-x@ 12 reader  staff    384 Sep  2 13:22 .git
-rw-r--r--@  1 reader  staff     57 Sep  2 13:08 .gitignore
drwxr-xr-x@  7 reader  staff    224 Sep  2 13:07 .venv
-rw-r--r--@  1 reader  staff    608 Sep  2 13:21 CLAUDE.md
-rw-r--r--@  1 reader  staff  32297 Sep  2 13:20 SPEC.md
--- tree ---
.
./.claude
./.gitignore
./.venv
./SPEC.md
./CLAUDE.md
./.claude/settings.json
./.venv/bin
./.venv/include
./.venv/pyvenv.cfg
./.venv]

[tool: Bash {"command": "ls .venv/lib/python3.14/site-packages/ | grep -i 'dist-info' | sort && echo \"--- pip list ---\" && .venv/bin/python -m pip list 2>/dev/null | head -40 && echo \"--- build tools ---\" && .venv/bin/python -c \"import setuptools, sys; print('setuptools', setuptools.__version__)\" 2>&1; .v]
[result: ast_serialize-0.8.0.dist-info
coverage-7.16.0.dist-info
hypothesis-6.167.1.dist-info
iniconfig-2.3.0.dist-info
librt-0.15.0.dist-info
mypy-2.3.1.dist-info
mypy_extensions-1.1.0.dist-info
packaging-26.3.dist-info
pathspec-1.1.1.dist-info
pip-26.2.1.dist-info
pluggy-1.6.0.dist-info
pygments-2.21.0.dist-info
pytest-9.1.1.dist-info
pytest_cov-7.1.0.dist-info
ruff-0.16.5.dist-info
sortedcontainers-2.4.0.dist-info
typing_extensions-4.16.0.dist-info
--- pip list ---
Package           Version
----------------- -------
ast_serialize     0.8.0
coverage          7.16.0
hypothesis        6.167.1
iniconfig]

[tool: ToolSearch {"query": "select:AskUserQuestion,ExitPlanMode", "max_results": 2}]
[result: No matching deferred tools found]

Claude: Repo is greenfield (SPEC.md, CLAUDE.md, a 3.14 venv with pytest/hypothesis/ruff/mypy, no build backend installed). Nothing to explore, so I went straight to design. Writing the plan now.

[tool: Write {"file_path": "/Users/reader/.claude/plans/spec-md-claude-md-plan-the-memoized-whisper.md", "content": "# logsift v1 \u2014 project structure and build order\n\n## Context\n\nThe repo currently holds only `SPEC.md`, `CLAUDE.md`, a `.gitignore`, and a venv with\nthe dev tools (pytest 9.1, pytest-cov,]
[result: File created successfully at: /Users/reader/.claude/plans/spec-md-claude-md-plan-the-memoized-whisper.md (file state is current in your context — no need to Read it back)]

Claude: Plan written to `/Users/reader/.claude/plans/spec-md-claude-md-plan-the-memoized-whisper.md`. Summary:

**Layout** — `src/logsift/` exactly as SPEC §12, setuptools backend with the version read from `logsift.__version__` (no second copy in metadata), console script `logsift = logsift.cli:main`, dev extra adding `build` for the packaging gate.

**Seams that matter most:**

- Entry points only exist after an install, so `pip install -e .` is step 0 and the built-in entry points get declared later (step 6) with a reinstall. An entry point pointing at a module that doesn't exist yet breaks discovery for every earlier test.
- `expr/eval.py` owns three functions the rest of the tool reuses: `resolve_field` (also used by `--columns` and `count by`), `render_filter_str` (also the `count by` group key, since §9 defers to §6.3), and `coerce_number` (also p50/p95). Without that, §6.3 gets reimplemented three times.
- The reader stays dumb about blank lines and yields linenos for all of them; the pipeline counts blanks once. Otherwise replaying the sniff sample either double-counts blanks or drifts the line numbers.
- Preflight opens every input (and forces the gzip header check) before any output, because §5 requires exit 2 before a byte is written.
- `plugin.py` validates a loaded object with explicit attribute checks, not `isinstance` — better errors, and `issubclass` on a data protocol is a TypeError trap.

**Order** — 14 steps, each green: skeleton → record → timeparse → expr → plugin + fake-dist fixture → the two parsers → entry points → reader → sniff → pipeline → agg → render → cli (subprocess e2e) → properties + packaging. The one constraint worth defending is plugin before parsers, so the built-ins are written against the published contract rather than the contract being back-fitted to them.

**Two things I need you to settle before I start:**

1. **setuptools or hatchling?** You said setuptools; SPEC.md §2 says hatchling, and CLAUDE.md makes the spec binding. I'll go with setuptools and amend SPEC.md §2 in the same commit unless you'd rather keep hatchling.
2. **Quoted ISO 8601 literal — temporal or string?** §6.3's table says quoted timestamps are temporal, but the same section says quotes select string mode. I'll treat a quoted literal that starts with four digits and `-` and parses as ISO 8601 as temporal, everything else quoted as string. Cost: `path == "2026-09-01T00:00:00Z"` can never be a string compare.

One smaller call I made without asking: with zero matches, table mode prints the header row and its `-` separator. §8.2 says "only the header"; I read the separator as part of the header block. Say so if you want it bare.

[result: turns=5 cost=$1.17 session=504c076c-4238-a9b2-a742-bcf8969269ff]
