"""Render a claude -p stream-json file as a readable transcript."""
import json
import sys

STREAM, PROMPT = sys.argv[1], sys.argv[2]
print("## Prompt\n\n```\n" + open(PROMPT).read().rstrip() + "\n```\n\n## Session\n")
for ln in open(STREAM):
    try:
        m = json.loads(ln)
    except ValueError:
        continue
    t = m.get("type")
    if t == "assistant":
        for b in m["message"].get("content", []):
            if b.get("type") == "text":
                print("\nClaude: " + b["text"])
            elif b.get("type") == "tool_use":
                inp = json.dumps(b.get("input", {}))
                print(f"\n[tool: {b['name']} {inp[:300]}]")
    elif t == "user":
        c = m["message"].get("content", [])
        if isinstance(c, list):
            for b in c:
                if b.get("type") == "tool_result":
                    s = b.get("content")
                    if isinstance(s, list):
                        s = "".join(x.get("text", "") for x in s)
                    print(f"[result: {str(s)[:600]}]")
    elif t == "result":
        print(f"\n[result: turns={m.get('num_turns')} "
              f"cost=${m.get('total_cost_usd', 0):.2f} "
              f"session={m.get('session_id')}]")
