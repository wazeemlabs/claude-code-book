#!/usr/bin/env python3
"""Per-task and per-month cost estimate from Claude Code result JSON.

Feed it the result objects that `claude -p --output-format json` prints
(or the last line of a `stream-json` transcript, or the Agent SDK result
message). Each file is one task. The script reads `total_cost_usd` and
`modelUsage`, weights the tasks by the mix you expect, and projects the
spend per task, per day, and per month against the $13-per-developer-day
benchmark from Chapter 27 of Claude Code from the Ground Up.

    estimate.py run1.json run2.json --tasks-per-day 6
    estimate.py --mix small=8,big=1 small.json big.json

The costs are the client-side list-price estimates Claude Code writes
(`costBasis: list`). On a subscription they show what the same work would
cost on the API; on Bedrock, Vertex, or Foundry the provider's own bill is
the number that counts.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

BENCHMARK_USD_PER_DAY = 13.0


@dataclass(frozen=True)
class ModelLine:
    model: str
    cost_usd: float
    input_tokens: int
    output_tokens: int
    cache_read: int
    cache_write: int

    @property
    def cache_hit_ratio(self) -> float:
        prompt = self.input_tokens + self.cache_read + self.cache_write
        return self.cache_read / prompt if prompt else 0.0


@dataclass(frozen=True)
class Task:
    label: str
    total_cost_usd: float
    num_turns: int
    models: tuple[ModelLine, ...]


def parse_result(label: str, data: dict) -> Task:
    """Shape one result object. Raises ValueError on a missing contract."""
    if data.get("type") not in (None, "result"):
        raise ValueError(f"{label}: not a result message (type={data['type']!r})")
    if "total_cost_usd" not in data:
        raise ValueError(f"{label}: no total_cost_usd field")
    usage = data.get("modelUsage") or data.get("model_usage") or {}
    models = tuple(
        ModelLine(
            model=name,
            cost_usd=float(m.get("costUSD", 0.0)),
            input_tokens=int(m.get("inputTokens", 0)),
            output_tokens=int(m.get("outputTokens", 0)),
            cache_read=int(m.get("cacheReadInputTokens", 0)),
            cache_write=int(m.get("cacheCreationInputTokens", 0)),
        )
        for name, m in sorted(usage.items())
    )
    return Task(
        label=label,
        total_cost_usd=float(data["total_cost_usd"]),
        num_turns=int(data.get("num_turns", 0)),
        models=models,
    )


def load_task(path: Path) -> Task:
    """Read a JSON result, or the last result line of a stream-json file."""
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".jsonl":
        results = [
            json.loads(line) for line in text.splitlines()
            if line.strip() and '"type":"result"' in line.replace(" ", "")
        ]
        if not results:
            raise ValueError(f"{path}: no result line in stream")
        return parse_result(path.stem, results[-1])
    return parse_result(path.stem, json.loads(text))


def parse_mix(spec: str | None, labels: list[str]) -> dict[str, float]:
    """`small=8,big=1` -> weights; unnamed tasks weigh 1."""
    weights = {label: 1.0 for label in labels}
    if not spec:
        return weights
    for item in spec.split(","):
        name, _, raw = item.partition("=")
        name = name.strip()
        if name not in weights:
            raise ValueError(f"--mix names {name!r}, which is not a task")
        try:
            weight = float(raw)
        except ValueError:
            raise ValueError(f"--mix weight for {name!r} is not a number")
        if weight < 0:
            raise ValueError(f"--mix weight for {name!r} is negative")
        weights[name] = weight
    return weights


@dataclass(frozen=True)
class Estimate:
    per_task: float
    per_day: float
    per_month: float
    vs_benchmark: float


def estimate(tasks: list[Task], mix: dict[str, float],
             tasks_per_day: float, days_per_month: float) -> Estimate:
    total_weight = sum(mix[t.label] for t in tasks)
    if total_weight <= 0:
        raise ValueError("the task mix weighs zero; nothing to estimate")
    per_task = sum(t.total_cost_usd * mix[t.label] for t in tasks) / total_weight
    per_day = per_task * tasks_per_day
    return Estimate(
        per_task=per_task,
        per_day=per_day,
        per_month=per_day * days_per_month,
        vs_benchmark=per_day / BENCHMARK_USD_PER_DAY,
    )


def render(tasks: list[Task], mix: dict[str, float], est: Estimate,
           tasks_per_day: float, days_per_month: float) -> str:
    width = max(4, *(len(t.label) for t in tasks))
    lines = [f"{'task':<{width}} weight   turns      cost   "
             "models (cache hit)"]
    for t in tasks:
        models = ", ".join(
            f"{m.model} {m.cache_hit_ratio:.0%}" for m in t.models) or "-"
        lines.append(f"{t.label:<{width}} {mix[t.label]:>6g} "
                     f"{t.num_turns:>7} {t.total_cost_usd:>9.2f}   {models}")
    lines += [
        "",
        f"per task   ${est.per_task:,.2f}  (weighted by the mix)",
        f"per day    ${est.per_day:,.2f}  at {tasks_per_day:g} tasks a day",
        f"per month  ${est.per_month:,.2f}  over {days_per_month:g} "
        "working days",
        f"benchmark  {est.vs_benchmark:.2f}x the ${BENCHMARK_USD_PER_DAY:.0f}"
        "-a-day enterprise average",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("files", nargs="+", type=Path,
                    help="result JSON files, or stream-json .jsonl transcripts")
    ap.add_argument("--tasks-per-day", type=float, default=4.0)
    ap.add_argument("--days-per-month", type=float, default=20.0)
    ap.add_argument("--mix", help="task weights, e.g. small=8,big=1")
    ap.add_argument("--json", action="store_true",
                    help="print the estimate as JSON instead of a table")
    args = ap.parse_args(argv)

    try:
        tasks = [load_task(p) for p in args.files]
        mix = parse_mix(args.mix, [t.label for t in tasks])
        est = estimate(tasks, mix, args.tasks_per_day, args.days_per_month)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"estimate.py: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(est.__dict__, indent=2))
    else:
        print(render(tasks, mix, est, args.tasks_per_day, args.days_per_month))
    return 0


if __name__ == "__main__":
    sys.exit(main())
