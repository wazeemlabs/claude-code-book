# Cost estimator (Chapter 27)

Turns the result objects Claude Code prints into a per-task, per-day, and
per-month estimate against the $13-per-developer-day benchmark.

Input is any of:

- the JSON object from `claude -p ... --output-format json`
- a `--output-format stream-json` transcript (`.jsonl`); the last
  `result` line is used
- the Agent SDK result message saved as JSON (`modelUsage` or the Python
  SDK's `model_usage`)

```
python3 estimate.py run1.json run2.json --tasks-per-day 6
python3 estimate.py --mix small=8,big=1 small.json big.json
python3 estimate.py ../transcripts/ch08/1*.jsonl --json
```

`--mix` weights tasks by how often each kind happens; unnamed tasks weigh
1. Per-model lines show the cache hit ratio (cache reads over all prompt
tokens), which is the first thing to look at when a task costs more than
it should.

A transcript that was interrupted before its result line (chapter 8's
`03-step1.jsonl`, resumed in `03b`) is reported as an error, not guessed.

Costs are Claude Code's list-price estimates (`costBasis: list`). Tests:
`python3 -m pytest -q` in this folder.
