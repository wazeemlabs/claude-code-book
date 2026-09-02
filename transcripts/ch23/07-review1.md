## Prompt

```
/code-review
```

## Session


Claude: `scripts/full-suite-gate.sh:1` — Stop hook exits 2 whenever the suite is red but never checks `stop_hook_active` from the hook JSON, so a persistently failing test blocks the turn from ending and re-invokes Claude in a loop.
`.claude/settings.json:9` — deny list only covers `Edit(helpdesk/migrations/**)`; `Write` to the same path is still allowed, so the migration-history guard CLAUDE.md relies on can be bypassed by writing the file whole.
`scripts/test-touched.sh:16` — on failure the output is filtered through `grep -E '^(FAIL|ERROR):|^Ran |^FAILED'`; an import error or a traceback with no matching line prints nothing to stderr, so Claude gets exit 2 with an empty reason.

[result: turns=0 cost=$0.32 session=48ed727b-5389-45e9-3bcd-4d66e202c1c1]
