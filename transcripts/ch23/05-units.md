## Prompt

```
Using docs/migration/inventory.md, split the migration
from Django 4.2 to Django 5.2 into independent units.
Each unit: one module or a tightly coupled pair, its
tests, and no shared files with any other unit. Order
them lowest risk first. For each, write the exact
prompt a subagent would need to do it, including the
verification command. A second virtual environment,
.venv52, has Django 5.2 installed; a unit is verified
with .venv52/bin/python quicktest.py <its test modules>
and the baseline is kept green with .venv/bin/python
quicktest.py. Write the result to
docs/migration/units.md. Do not start any.
```

## Session


Claude: I'll start by reading the inventory and related docs.

[tool: Read {"file_path": "/Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield/docs/migration/inventory.md"}]
[result: 1	# Django 4.2 -> 5.2 migration inventory
2	
3	Baseline: Django 4.2.30 installed in `.venv`. `constraints-Django5.txt` already pins
4	`Django >=5,<6`, so the target is 5.2 LTS.
5	
6	This document is an inventory only. It lists, per module, the framework surfaces the
7	code touches, the tests that exercise those files, and a risk rating.
8	
9	Risk ratings mean:
10	
11	- **High** - a known removal or behaviour change in 5.0/5.1/5.2 hits this code, or a
12	  large surface is exercised with thin tests.
13	- **Medium** - the module uses framework surfaces that changed, but the specific calls
14	  l]

[tool: Bash {"command": "ls /Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield/docs/migration/ && ls /Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield/helpdesk/tests/", "description": "List migration docs and tests"}]
[result: inventory.md
__init__.py
__pycache__
helpers.py
test_api.py
test_attachments.py
test_checklist.py
test_files
test_get_email.py
test_kb.py
test_login.py
test_markdown.py
test_navigation.py
test_per_queue_staff_permission.py
test_public_actions.py
test_query.py
test_savequery.py
test_ticket_actions.py
test_ticket_lookup.py
test_ticket_submission.py
test_time_spent.py
test_time_spent_auto.py
test_usersettings.py
test_webhooks.py
urls.py
utils.py]

[tool: Bash {"command": "ls -d .venv .venv52 2>&1; .venv/bin/python -c \"import django;print(django.get_version())\" 2>&1; .venv52/bin/python -c \"import django;print(django.get_version())\" 2>&1; ls docs/migration/pattern.md 2>&1; grep -rn \"USE_L10N\\|DEFAULT_FILE_STORAGE\\|STORAGES\" --include=*.py . | grep ]
[result: .venv
.venv52
4.2.30
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'django'
ls: docs/migration/pattern.md: No such file or directory
(eval):1: no matches found: --include=*.py]

[tool: Bash {"command": "ls .venv52/lib/*/site-packages | head -40; ls .venv52/bin", "description": "Inspect .venv52"}]
[result: _distutils_hack
distutils-precedence.pth
pip
pip-26.2.1.dist-info
pkg_resources
setuptools
setuptools-80.9.0.dist-info
Activate.ps1
activate
activate.csh
activate.fish
pip
pip3
pip3.11
python
python3
python3.11]

[tool: Bash {"command": "grep -rn \"USE_L10N\\|DEFAULT_FILE_STORAGE\\|STORAGES\" --include=\"*.py\" helpdesk demo standalone; echo ---; grep -rln \"form.as_p\\|{{ form }}\" helpdesk/templates | head; echo ---; sed -n 1,40p quicktest.py; echo ---; ls; cat constraints-Django5.txt 2>/dev/null", "description": "Gre]
[result: helpdesk/models.py:1278:            settings.DEFAULT_FILE_STORAGE
helpdesk/models.py:1299:            settings.DEFAULT_FILE_STORAGE
demo/demodesk/config/settings.py:214:USE_L10N = True
standalone/config/settings.py:220:USE_L10N = True
---
helpdesk/templates/helpdesk/checklist_templates.html
helpdesk/templates/helpdesk/ticket.html
---
#!/usr/bin/env python
"""
Usage:
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements-testing.txt -r requirements.txt
$ python ./quicktest.py
"""

import argparse
import django
from django.conf import settings
import os
import sys


cla]

[tool: Bash {"command": "sed -n 1270,1310p helpdesk/models.py; echo ===; sed -n 40,120p quicktest.py", "description": "Read attachment_path and quicktest settings"}]
[result: Exit code 1
    def attachment_path(self, filename):
        path = "helpdesk/attachments/{ticket_for_url}-{secret_key}/{id_}".format(
            ticket_for_url=self.followup.ticket.ticket_for_url,
            secret_key=self.followup.ticket.secret_key,
            id_=self.followup.id,
        )
        att_path = os.path.join(settings.MEDIA_ROOT, path)
        if (
            settings.DEFAULT_FILE_STORAGE
            == "django.core.files.storage.FileSystemStorage"
        ):
            if not os.path.exists(att_path):
                os.makedirs(att_path, helpdesk_settings.HELPDESK_ATTAC]

[tool: Bash {"command": "sed -n 40,130p quicktest.py", "description": "Read quicktest settings"}]
[result:         #  The following commented apps are optional,
        #  related to teams functionalities
        # 'account',
        # 'pinax.invitations',
        # 'pinax.teams',
        "rest_framework",
        "helpdesk",
        # 'reversion',
    )
    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.midd]

[tool: Bash {"command": "cat requirements.txt requirements-testing.txt; grep -n \"Django\\|classifiers\" -A15 setup.py | head -60; sed -n 1,60p tox.ini", "description": "Read deps and packaging"}]
[result: Django>=3.2
django-bootstrap4-form
celery
email-reply-parser
akismet
markdown
beautifulsoup4
lxml
pytz
pinax_teams
djangorestframework
django-model-utils
django-cleanup
oauthlib
requests_oauthlib
requests
pysocks
pycodestyle
coverage
argparse
pbr
mock
freezegun
isort
numpy
factory_boy
faker133:    description="Django-powered ticket tracker for your helpdesk",
134-    long_description_content_type="text/x-rst",
135-    long_description=get_long_description(),
136:    classifiers=[
137-        "Development Status :: 4 - Beta",
138-        "Programming Language :: Python",
139-        "Programmin]

[tool: Write {"file_path": "/Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield/docs/migration/units.md", "content": "# Django 4.2 -> 5.2 migration units\n\nSplit of the work described in `docs/migration/inventory.md` into units that can be\ndone by one subagent each, in any order, without two ]
[result: File created successfully at: /Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield/docs/migration/units.md (file state is current in your context — no need to Read it back)]

Claude: Written to `docs/migration/units.md`. Ten units, each owning an exclusive set of source files and test modules, ordered lowest risk first, each with a ready-to-paste subagent prompt and its two verification commands.

Three things worth knowing:

1. **`.venv52` does not have Django 5.2 installed.** It contains only pip and setuptools — `.venv52/bin/python -c "import django"` fails. Nothing can be verified until it's populated; I put the install command at the top of the doc. `.venv` is fine (4.2.30).

2. **The ordering has one dependency exception.** `helpdesk/models.py:1278` and `:1299` read `settings.DEFAULT_FILE_STORAGE`, removed in 5.1, and no settings file in the repo (including `quicktest.py`) defines it. Any test that uploads an attachment will `AttributeError` under 5.2 until Unit 8 lands — that hits Unit 7 (`test_get_email`) and Unit 9 (`test_ticket_submission`). So the practical order is 1, 2, 3, 4, 5, 6, **8**, 7, 9, 10, not strictly risk-ascending. Both orders are stated in the doc.

3. **CLAUDE.md points at `docs/migration/pattern.md`, which doesn't exist.** It's cited as the required procedure for touching the two High-risk modules. Units 8 and 10 currently carry their own constraints inline instead. Worth either writing that file or dropping the reference.

Two units (1 and 3) own surfaces with no existing tests; Unit 1 creates `test_templatetags.py` and `test_admin.py` so it has something to verify against, and Unit 3 verifies through `manage.py check` on both projects plus a full-suite regression run, since settings files aren't exercised by `quicktest.py` at all.

[result: turns=10 cost=$1.05 session=a5282339-fe56-c0dc-3d83-981832a90b60]
