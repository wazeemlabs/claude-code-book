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

## How the sessions were billed

Every session here (the `claude -p` runs and the Agent SDK runs) used a
claude.ai subscription login, not an API key. The dollar figures in the
run logs and transcripts are Claude Code's own estimates at list price
(`costBasis: list`); the usage actually counted against the plan's
five-hour and weekly windows. Fast mode was off. An SDK agent shipped to
other people must use an API key or a cloud provider (see Chapter 24);
running it locally under your own login, as here, is fine.
