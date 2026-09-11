# Companion sessions for Claude Code from the Ground Up

- logsift, logsift-nginx: Chapter 8 project and plugin, separate repos at
  github.com/wazeemlabs/logsift and github.com/wazeemlabs/logsift-nginx
- brownfield: Chapter 23, django-helpdesk at 73b19cd4, migrated 4.2 -> 5.2, at
  github.com/wazeemlabs/django-helpdesk-migration (branches
  migration-baseline, migration-integration, migrate/unit-N)
- transcripts/ch08, transcripts/ch23: every session as stream-json
  (.jsonl), rendered (.md), with the prompt used (.prompt)
- triage-agent: Chapter 24, the Agent SDK triage agent with its run logs
- cost-estimator: Chapter 27, per-task and per-month estimate from result JSON
- aplus: the Amazon A+ content (module copy, images, sources)
- the companion site is books.wazeem.com/claude-code, built from books/site
- tools/run.sh, tools/render.py: run and render a headless session
- tools/interview.py: drive AskUserQuestion through the Agent SDK

## Redactions

The transcripts are published as recorded, except for these edits:

- The author's username reads `reader`, in paths (`/Users/reader/...`)
  and in `ls -l` output.
- Session ids, message ids, API request ids, tool-call ids, and agent
  and task ids are random stand-ins of the same shape. Each original
  maps to one stand-in, so every tool call still pairs with its result.
- The author's own MCP servers and their tools read `(redacted)` in each
  session's init event. No session called any of them.
- In transcripts/ch23/01-overview, a `ListAgents` call listed the
  author's other local Claude Code sessions; the names of six that have
  nothing to do with the book read `(redacted)`.

Nothing else is edited. The `.md` renders are regenerated from the
edited `.jsonl` with tools/render.py, and the turn counts and costs the
book quotes are unchanged.

## How the sessions were billed

Every session here (the `claude -p` runs and the Agent SDK runs) used a
claude.ai subscription login, not an API key. The dollar figures in the
run logs and transcripts are Claude Code's own estimates at list price
(`costBasis: list`); the usage actually counted against the plan's
five-hour and weekly windows. Fast mode was off. An SDK agent shipped to
other people must use an API key or a cloud provider (see Chapter 24);
running it locally under your own login, as here, is fine.
