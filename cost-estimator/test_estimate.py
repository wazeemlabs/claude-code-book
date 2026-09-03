"""Run: python3 -m pytest cost-estimator/ -q"""

import json
from pathlib import Path

import pytest

import estimate as e

HERE = Path(__file__).resolve().parent
TRANSCRIPTS = HERE.parent / "transcripts"


def result(cost, models=None, **extra):
    data = {"type": "result", "total_cost_usd": cost, "num_turns": 3,
            "modelUsage": models or {}}
    data.update(extra)
    return data


def test_parses_total_and_per_model_lines():
    t = e.parse_result("a", result(1.5, {
        "claude-opus-5": {"costUSD": 1.5, "inputTokens": 10,
                          "outputTokens": 20, "cacheReadInputTokens": 70,
                          "cacheCreationInputTokens": 20}}))
    assert t.total_cost_usd == 1.5
    assert t.models[0].model == "claude-opus-5"
    assert t.models[0].cache_hit_ratio == pytest.approx(0.7)


def test_accepts_python_sdk_snake_case_model_usage():
    t = e.parse_result("a", {"total_cost_usd": 0.2,
                             "model_usage": {"m": {"costUSD": 0.2}}})
    assert t.models[0].cost_usd == 0.2


def test_rejects_object_without_total_cost():
    with pytest.raises(ValueError, match="no total_cost_usd"):
        e.parse_result("a", {"type": "result"})


def test_rejects_non_result_message():
    with pytest.raises(ValueError, match="not a result"):
        e.parse_result("a", {"type": "assistant", "total_cost_usd": 1})


def test_cache_hit_ratio_is_zero_with_no_prompt_tokens():
    line = e.ModelLine("m", 0.0, 0, 5, 0, 0)
    assert line.cache_hit_ratio == 0.0


def test_loads_last_result_line_of_stream_json(tmp_path):
    p = tmp_path / "s.jsonl"
    p.write_text("\n".join([
        json.dumps({"type": "assistant"}),
        json.dumps(result(0.5)),
        json.dumps(result(0.9)),
    ]))
    assert e.load_task(p).total_cost_usd == 0.9


def test_stream_without_result_line_is_an_error(tmp_path):
    p = tmp_path / "s.jsonl"
    p.write_text(json.dumps({"type": "assistant"}) + "\n")
    with pytest.raises(ValueError, match="no result line"):
        e.load_task(p)


@pytest.mark.skipif(not TRANSCRIPTS.exists(), reason="no transcripts")
def test_reads_a_real_chapter_8_transcript():
    t = e.load_task(TRANSCRIPTS / "ch08" / "06-logfmt.jsonl")
    assert t.total_cost_usd == pytest.approx(5.3428205)
    assert {m.model for m in t.models} == {"claude-opus-4-6", "claude-opus-5"}
    assert sum(m.cost_usd for m in t.models) == pytest.approx(
        t.total_cost_usd, rel=1e-6)


def test_mix_defaults_every_task_to_weight_one():
    assert e.parse_mix(None, ["a", "b"]) == {"a": 1.0, "b": 1.0}


def test_mix_overrides_named_tasks_only():
    assert e.parse_mix("a=8", ["a", "b"]) == {"a": 8.0, "b": 1.0}


@pytest.mark.parametrize("spec,msg", [
    ("zz=1", "not a task"),
    ("a=x", "not a number"),
    ("a=-1", "negative"),
])
def test_mix_rejects_bad_specs(spec, msg):
    with pytest.raises(ValueError, match=msg):
        e.parse_mix(spec, ["a"])


def test_weighted_estimate_and_benchmark_ratio():
    tasks = [e.Task("small", 0.5, 1, ()), e.Task("big", 5.0, 1, ())]
    est = e.estimate(tasks, {"small": 9, "big": 1}, tasks_per_day=10,
                     days_per_month=20)
    # (0.5*9 + 5.0*1) / 10 = 0.95 per task
    assert est.per_task == pytest.approx(0.95)
    assert est.per_day == pytest.approx(9.5)
    assert est.per_month == pytest.approx(190.0)
    assert est.vs_benchmark == pytest.approx(9.5 / 13)


def test_zero_weight_mix_is_an_error():
    with pytest.raises(ValueError, match="weighs zero"):
        e.estimate([e.Task("a", 1.0, 1, ())], {"a": 0}, 1, 1)


def test_cli_returns_2_and_explains_on_bad_input(tmp_path, capsys):
    p = tmp_path / "bad.json"
    p.write_text("{}")
    assert e.main([str(p)]) == 2
    assert "no total_cost_usd" in capsys.readouterr().err


def test_cli_json_output_has_the_four_numbers(tmp_path, capsys):
    p = tmp_path / "t.json"
    p.write_text(json.dumps(result(2.0)))
    assert e.main([str(p), "--json", "--tasks-per-day", "1",
                   "--days-per-month", "1"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out == {"per_task": 2.0, "per_day": 2.0, "per_month": 2.0,
                   "vs_benchmark": pytest.approx(2 / 13)}
