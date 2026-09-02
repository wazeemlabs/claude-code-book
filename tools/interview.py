"""Run one Claude Code session through the Agent SDK, answering
AskUserQuestion by hand: questions land in q.json, the driver waits
for a.json, and every message is appended to a transcript file.

Usage: python tools/interview.py <cwd> <transcript.md> <prompt-file>
"""
import asyncio
import json
import os
import sys
import time

from claude_agent_sdk import (
    AssistantMessage, ClaudeAgentOptions, ClaudeSDKClient,
    PermissionResultAllow, ResultMessage, TextBlock, ToolResultBlock,
    ToolUseBlock, UserMessage,
)

CWD, OUT, PROMPT_FILE = sys.argv[1:4]
QFILE = os.path.join(os.path.dirname(OUT), "q.json")
AFILE = os.path.join(os.path.dirname(OUT), "a.json")


def log(s):
    with open(OUT, "a", encoding="utf-8") as f:
        f.write(s + "\n")


async def can_use_tool(name, inp, ctx):
    if name != "AskUserQuestion":
        return PermissionResultAllow()
    for f in (AFILE,):
        if os.path.exists(f):
            os.remove(f)
    with open(QFILE, "w") as f:
        json.dump(inp, f, indent=2)
    while not os.path.exists(AFILE):
        await asyncio.sleep(2)
    time.sleep(1)
    with open(AFILE) as f:
        answers = json.load(f)
    os.remove(QFILE)
    os.remove(AFILE)
    for q in inp.get("questions", []):
        log(f"\n> Q: {q['question']}")
        for o in q.get("options", []):
            log(f">   - {o['label']}: {o.get('description','')}")
        log(f"> A: {answers.get(q['question'], '(no answer)')}")
    return PermissionResultAllow(
        updated_input={"questions": inp.get("questions", []),
                       "answers": answers})


async def main():
    prompt = open(PROMPT_FILE).read()
    log(f"## Prompt\n\n```\n{prompt}```\n\n## Session\n")
    opts = ClaudeAgentOptions(
        cwd=CWD, model="opus", permission_mode="acceptEdits",
        can_use_tool=can_use_tool,
        setting_sources=["user", "project"],
    )
    async with ClaudeSDKClient(options=opts) as c:
        await c.query(prompt)
        async for m in c.receive_response():
            if isinstance(m, AssistantMessage):
                for b in m.content:
                    if isinstance(b, TextBlock):
                        log(f"\nClaude: {b.text}")
                    elif isinstance(b, ToolUseBlock):
                        if b.name != "AskUserQuestion":
                            log(f"\n[tool: {b.name} "
                                f"{json.dumps(b.input)[:200]}]")
            elif isinstance(m, UserMessage) and not isinstance(
                    m.content, str):
                for b in m.content:
                    if isinstance(b, ToolResultBlock):
                        s = b.content if isinstance(b.content, str) \
                            else json.dumps(b.content)
                        log(f"[result: {s[:300]}]")
            elif isinstance(m, ResultMessage):
                log(f"\n[result: turns={m.num_turns} "
                    f"cost=${m.total_cost_usd:.2f} "
                    f"session={m.session_id}]")
                print(json.dumps({"turns": m.num_turns,
                                  "cost": m.total_cost_usd,
                                  "session": m.session_id}))


asyncio.run(main())
