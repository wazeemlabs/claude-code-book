#!/bin/bash
# Run one headless Claude Code session and keep the raw stream.
# Usage: tools/run.sh <cwd> <transcript-basename> <prompt-file> [claude flags...]
set -u
HERE=$(cd "$(dirname "$0")" && pwd)   # before the cd below
CWD=$1; OUT=$2; PROMPT=$3; shift 3
cd "$CWD"
source .venv/bin/activate 2>/dev/null || true
env -u CLAUDECODE claude -p "$(cat "$PROMPT")" --model opus \
  --output-format stream-json --verbose "$@" < /dev/null > "$OUT.jsonl" 2> "$OUT.stderr"
python3 "$HERE/render.py" "$OUT.jsonl" "$PROMPT" > "$OUT.md"
tail -1 "$OUT.jsonl" | python3 -c '
import json,sys
r=json.loads(sys.stdin.read())
print({k:r.get(k) for k in ("num_turns","total_cost_usd","subtype","session_id","terminal_reason")})'
