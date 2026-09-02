## Prompt

```
Revise CLAUDE.md so it contains only what a competent
engineer could not infer from the code: the test
command and how to run one file, the two directories
that must not be edited without a migration, the naming
convention for services, and the fact that the modules
docs/migration/inventory.md rates High have thin direct
tests and must be changed only behind the pattern in
docs/migration/pattern.md. Under 60 lines. Delete
anything the code already makes obvious.
```

## Session


[tool: Bash {"command": "cd /Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield; ls docs/migration; grep -rn \"High\" docs/migration/inventory.md | head -20", "description": "Check pattern.md and High-rated modules"}]
[result: inventory.md
docs/migration/inventory.md:11:- **High** - a known removal or behaviour change in 5.0/5.1/5.2 hits this code, or a
docs/migration/inventory.md:60:| `helpdesk/models.py` | `settings.DEFAULT_FILE_STORAGE`, `models.*`, `Model.save(*args)`, `timezone.now`, `mark_safe`, `ContentType`, `Permission`, `reverse` | Indirect only, via `test_ticket_submission.py`, `test_attachments.py`, `test_ticket_actions.py`, `test_time_spent*.py`, `test_kb.py` | **High** |
docs/migration/inventory.md:61:| `helpdesk/views/staff.py` | `FormView`, `UpdateView`, `Paginator`, `inlineformset_factory`, `user_pa]

[tool: Bash {"command": "cd /Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield; find . -path ./.venv -prune -o -name migrations -type d -print; grep -rn \"service\" --include=*.py -il helpdesk | head", "description": "Find migrations dirs and service naming"}]
[result: ./helpdesk/migrations
(eval):1: no matches found: --include=*.py]

[tool: Bash {"command": "cd /Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield; grep -rln \"service\" helpdesk --include='*.py' | head; echo ---; grep -rn \"services:\" standalone/docker-compose.yml -A20 | head -30", "description": "Look for services"}]
[result: ---
standalone/docker-compose.yml:8:services:
standalone/docker-compose.yml-9-  caddy:
standalone/docker-compose.yml-10-    image: caddy:2
standalone/docker-compose.yml-11-    restart: unless-stopped
standalone/docker-compose.yml-12-    volumes:
standalone/docker-compose.yml-13-      - caddy_data:/data
standalone/docker-compose.yml-14-      - caddy_config:/config
standalone/docker-compose.yml-15-      - ./Caddyfile:/etc/caddy/Caddyfile:ro
standalone/docker-compose.yml-16-    ports:
standalone/docker-compose.yml-17-      - "80:80"
standalone/docker-compose.yml-18-      - "443:443"
standalone/do]

[tool: Write {"file_path": "/Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield/CLAUDE.md", "content": "# CLAUDE.md\n\nThis file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.\n\n## Tests\n\n`manage.py test` is not the entry point. `quicktest.py` ca]
[result: The file /Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield/CLAUDE.md has been updated successfully. (file state is current in your context — no need to Read it back)]

Claude: Rewrote it at 36 lines. Everything the code makes obvious is gone — architecture, request flow, settings indirection, ruff, CI matrix, conventions.

Three things I could not source, so I did not invent them:

- **`docs/migration/pattern.md` does not exist.** Only `inventory.md` is in `docs/migration/`. I wrote the rule pointing at that path as you specified, but the file needs to be created or the reference is a dead end.
- **Naming convention for services — I found nothing to describe.** No service layer in `helpdesk/` (no module, class, or directory using the term), and the only "services" in the repo are the docker-compose entries in `standalone/docker-compose.yml` (`caddy`, `django-helpdesk`, `postgres`). If you meant that convention, tell me the rule and I'll add it; I'm not going to guess it from three container names.
- **Only one directory is migration-gated,** `helpdesk/migrations/`. For the second I used `helpdesk/models.py`, since that's what actually forces a migration — but it's a file, not a directory. If you had a different second directory in mind, say which.

[result: turns=5 cost=$0.61 session=caa72432-70e5-3e91-ab80-414d7272a382]
