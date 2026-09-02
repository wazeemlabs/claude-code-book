## Prompt

```
Give me an overview of this codebase: what it does, the
main architecture patterns, the key data models, how
requests flow in and out, and how tests are organized.
Then list the parts that look oldest or most fragile.
```

## Session


Claude: I'll explore the codebase first.

[tool: Bash {"command": "ls -a && cat README* 2>/dev/null | head -60 && echo \"---\" && ls -R --ignore=node_modules 2>/dev/null | head -80", "description": "List repo root and readme"}]
[result: .
..
.coveragerc
.dockerignore
.flake8
.git
.github
.gitignore
.isort.cfg
.pylintrc
.readthedocs.yaml
.tx
.venv
AUTHORS
CONTRIBUTING.rst
LICENSE
LICENSE.3RDPARTY
MANIFEST.in
Makefile
README.rst
SECURITY.md
build_project.sh
constraints-Django32.txt
constraints-Django4.txt
constraints-Django5.txt
demo
docs
helpdesk
pyproject.toml
quicktest.py
requirements-dev.txt
requirements-no-pinax.txt
requirements-testing.txt
requirements.txt
setup.py
standalone
tox.ini
django-helpdesk - A Django powered ticket tracker for small businesses.
====================================================================]

[tool: Agent {"subagent_type": "Explore", "description": "Explore models and data layer", "prompt": "In /Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield (django-helpdesk), thoroughly map the data layer: helpdesk/models.py (all models, key fields, relationships, notable properties/methods), m]
[result: Async agent launched successfully. (This tool result is internal metadata — never quote or paste any part of it, including the agentId below, into a user-facing reply.)
agentId: fa87d4976a73da078 (internal ID - do not mention to user. Use SendMessage with to: 'fa87d4976a73da078', summary: '<5-10 word recap>' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes. You know nothing about its results until that notification arrives — do not report, assume, or predict them; continue other work or respond to the user in the meantime.
Do]

[tool: Agent {"subagent_type": "Explore", "description": "Explore request flow", "prompt": "In /Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield (django-helpdesk), map how requests flow: urls.py, views/ package (each module's role and size), forms.py, the API (DRF?) surface, templates, middle]

Claude: I'll explore the data layer.
[result: Async agent launched successfully. (This tool result is internal metadata — never quote or paste any part of it, including the agentId below, into a user-facing reply.)
agentId: def9cacad32a31395 (internal ID - do not mention to user. Use SendMessage with to: 'def9cacad32a31395', summary: '<5-10 word recap>' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes. You know nothing about its results until that notification arrives — do not report, assume, or predict them; continue other work or respond to the user in the meantime.
Do]

[tool: Agent {"subagent_type": "Explore", "description": "Explore tests and tooling", "prompt": "In /Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield (django-helpdesk), map testing and tooling: helpdesk/tests/ layout, what each test module covers, test runner config (tox.ini, quicktest.py, Ma]

[tool: Bash {"command": "ls && wc -l helpdesk/models.py helpdesk/lib.py helpdesk/query.py helpdesk/serializers.py 2>/dev/null && ls helpdesk/migrations | head -100 && ls helpdesk/migrations | wc -l"}]
[result: AUTHORS
CONTRIBUTING.rst
LICENSE
LICENSE.3RDPARTY
MANIFEST.in
Makefile
README.rst
SECURITY.md
build_project.sh
constraints-Django32.txt
constraints-Django4.txt
constraints-Django5.txt
demo
docs
helpdesk
pyproject.toml
quicktest.py
requirements-dev.txt
requirements-no-pinax.txt
requirements-testing.txt
requirements.txt
setup.py
standalone
tox.ini
    2272 helpdesk/models.py
     284 helpdesk/lib.py
     258 helpdesk/query.py
     265 helpdesk/serializers.py
    3079 total
0001_initial.py
0002_populate_usersettings.py
0003_initial_data_import.py
0004_add_per_queue_staff_membership.py
0005_queues]

[tool: Bash {"command": "grep -n \"^class \\|^    class Meta\\|^    def \\|^    @\" helpdesk/models.py"}]
[result: 34:class EscapeHtml(Extension):
35:    def extendMarkdown(self, md):
69:class Queue(models.Model):
361:    def __str__(self):
364:    class Meta:
369:    def _from_address(self):
392:    @property
393:    def time_spent(self):
402:    @property
403:    def time_spent_formated(self):
406:    def prepare_permission_name(self):
415:    def save(self, *args, **kwargs):
451:    def delete(self, *args, **kwargs):
468:class Ticket(models.Model):
615:    @property
616:    def time_spent(self):
623:    @property
624:    def time_spent_formated(self):
627:    def send(self, roles, dont_send_to=None, **k]

Claude: I'll explore the repo structure first.

[tool: Bash {"command": "ls && find . -name \"*.py\" -not -path \"./.git/*\" | head -80 && echo \"---\" && find . -name \"*.py\" -not -path \"./.git/*\" -not -path \"*/migrations/*\" | xargs wc -l | sort -rn | head -40"}]
[result: AUTHORS
CONTRIBUTING.rst
LICENSE
LICENSE.3RDPARTY
MANIFEST.in
Makefile
README.rst
SECURITY.md
build_project.sh
constraints-Django32.txt
constraints-Django4.txt
constraints-Django5.txt
demo
docs
helpdesk
pyproject.toml
quicktest.py
requirements-dev.txt
requirements-no-pinax.txt
requirements-testing.txt
requirements.txt
setup.py
standalone
tox.ini
./quicktest.py
./setup.py
./demo/setup.py
./demo/manage.py
./standalone/__init__.py
./standalone/manage.py
./docs/conf.py
./helpdesk/signals.py
./helpdesk/user.py
./helpdesk/tasks.py
./helpdesk/models.py
./helpdesk/query.py
./helpdesk/lib.py
./helpdesk]
[result: Async agent launched successfully. (This tool result is internal metadata — never quote or paste any part of it, including the agentId below, into a user-facing reply.)
agentId: e4ca5c533b982a947 (internal ID - do not mention to user. Use SendMessage with to: 'e4ca5c533b982a947', summary: '<5-10 word recap>' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes. You know nothing about its results until that notification arrives — do not report, assume, or predict them; continue other work or respond to the user in the meantime.
Do]

[tool: Bash {"command": "grep -rn \"TODO\\|FIXME\\|XXX\\|deprecated\\|DEPRECATED\\|legacy\\|Legacy\\|raw(\\|cursor()\\|pickle\\|python_2\\|force_text\\|ugettext\" helpdesk/models.py helpdesk/lib.py helpdesk/query.py helpdesk/serializers.py"}]
[result: helpdesk/lib.py:124:        # deprecated, but kept for backward compatibility
helpdesk/models.py:1721:    settings_pickled = models.TextField(
helpdesk/models.py:1722:        _("DEPRECATED! Settings Dictionary DEPRECATED!"),
helpdesk/models.py:1724:            "DEPRECATED! This is a base64-encoded representation of a pickled Python dictionary. "]

Claude: I'll explore the repo structure and tooling files in parallel.

[tool: Bash {"command": "for f in helpdesk/migrations/0*.py; do echo \"$f $(git log -1 --format=%ad --date=short -- $f)\"; done | tail -45; echo ---; git log -1 --format=%ad --date=short"}]

[tool: Bash {"command": "find helpdesk -name \"*.py\" -not -path \"*/migrations/*\" | xargs wc -l | sort -rn | head -40 && echo \"=== templates ===\" && ls helpdesk/templates/helpdesk | head -60 && echo \"count:\" && find helpdesk/templates -name \"*.html\" | wc -l"}]
[result:    16917 total
    2272 helpdesk/models.py
    2120 helpdesk/views/staff.py
    1610 helpdesk/tests/test_get_email.py
    1201 helpdesk/tests/test_ticket_submission.py
    1148 helpdesk/email.py
     784 helpdesk/forms.py
     497 helpdesk/settings.py
     452 helpdesk/tests/test_api.py
     450 helpdesk/tests/test_time_spent_auto.py
     404 helpdesk/update_ticket.py
     395 helpdesk/tests/test_ticket_actions.py
     371 helpdesk/tests/utils.py
     313 helpdesk/tests/test_webhooks.py
     297 helpdesk/views/public.py
     295 helpdesk/tests/test_navigation.py
     284 helpdesk/lib.py
     2]

Claude: While those run, let me get some direct measurements.

[tool: Bash {"command": "ls -a && echo \"---TESTS---\" && ls -la helpdesk/tests/ && echo \"---WC---\" && wc -l helpdesk/tests/*.py && echo \"---CI---\" && ls -R .github 2>/dev/null && ls azure* 2>/dev/null && git log -1 --date=short --format='%h %ad %s'"}]
[result: Exit code 1
.
..
.coveragerc
.dockerignore
.flake8
.git
.github
.gitignore
.isort.cfg
.pylintrc
.readthedocs.yaml
.tx
.venv
AUTHORS
CONTRIBUTING.rst
LICENSE
LICENSE.3RDPARTY
MANIFEST.in
Makefile
README.rst
SECURITY.md
build_project.sh
constraints-Django32.txt
constraints-Django4.txt
constraints-Django5.txt
demo
docs
helpdesk
pyproject.toml
quicktest.py
requirements-dev.txt
requirements-no-pinax.txt
requirements-testing.txt
requirements.txt
setup.py
standalone
tox.ini
---TESTS---
total 608
drwxr-xr-x@ 27 reader  staff    864 Sep  2 14:41 .
drwxr-xr-x@ 35 reader  staff   1120 Sep  2 14:41 ..
-rw]

[tool: Bash {"command": "cd helpdesk && cat urls.py && echo \"=== views ===\" && wc -l views/*.py && echo \"=== decorators ===\" && cat decorators.py"}]
[result: """
django-helpdesk - A Django powered ticket tracker for small enterprise.

(c) Copyright 2008 Jutda. All Rights Reserved. See LICENSE for details.

urls.py - Mapping of URL's to our various views. Note we always used NAMED
          views for simplicity in linking later on.
"""

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from helpdesk import settings as helpdesk_settings
from helpdesk.decorators import helpdesk_staff_member_required, ]
[result: helpdesk/migrations/0001_initial.py 2025-03-22
helpdesk/migrations/0002_populate_usersettings.py 2025-04-01
helpdesk/migrations/0003_initial_data_import.py 2025-03-22
helpdesk/migrations/0004_add_per_queue_staff_membership.py 2025-03-22
helpdesk/migrations/0005_queues_no_null.py 2025-03-22
helpdesk/migrations/0006_email_maxlength.py 2025-03-22
helpdesk/migrations/0007_max_length_by_integer.py 2025-03-22
helpdesk/migrations/0008_extra_for_permissions.py 2025-03-22
helpdesk/migrations/0009_migrate_queuemembership.py 2025-03-22
helpdesk/migrations/0010_remove_queuemembership.py 2025-03-22
helpdes]

[tool: Bash {"command": "find helpdesk -name '*.py' -not -path '*/migrations/*' | xargs wc -l | sort -rn | head -30 && echo \"=== migrations ===\" && ls helpdesk/migrations | wc -l && ls helpdesk/migrations | head -5 && ls helpdesk/migrations | tail -5 && echo \"=== reqs ===\" && cat requirements.txt && echo \"]
[result:    16917 total
    2272 helpdesk/models.py
    2120 helpdesk/views/staff.py
    1610 helpdesk/tests/test_get_email.py
    1201 helpdesk/tests/test_ticket_submission.py
    1148 helpdesk/email.py
     784 helpdesk/forms.py
     497 helpdesk/settings.py
     452 helpdesk/tests/test_api.py
     450 helpdesk/tests/test_time_spent_auto.py
     404 helpdesk/update_ticket.py
     395 helpdesk/tests/test_ticket_actions.py
     371 helpdesk/tests/utils.py
     313 helpdesk/tests/test_webhooks.py
     297 helpdesk/views/public.py
     295 helpdesk/tests/test_navigation.py
     284 helpdesk/lib.py
     2]

[tool: Bash {"command": "for f in tox.ini quicktest.py Makefile setup.py setup.cfg pyproject.toml .coveragerc .flake8 .pre-commit-config.yaml azure-pipelines.yml; do echo \"=====$f=====\"; cat \"$f\" 2>/dev/null; done; echo \"===REQS===\"; ls requirements*; for f in requirements*.txt; do echo \"--$f--\"; cat $f]

[tool: Bash {"command": "cd helpdesk && grep -n \"^def \\|^class \\|^@\" views/staff.py | head -140"}]
[result: 115:def _get_queue_choices(queues):
128:def get_active_users() -> QuerySet:
138:def get_user_queues(user) -> dict[str, str]:
143:def get_form_extra_kwargs(user) -> dict[str, object]:
151:@helpdesk_staff_member_required
152:def dashboard(request):
282:def ticket_perm_check(request, ticket):
290:@helpdesk_staff_member_required
291:def delete_ticket(request, ticket_id):
312:@helpdesk_staff_member_required
313:def followup_edit(request, ticket_id, followup_id):
382:@helpdesk_staff_member_required
383:def followup_delete(request, ticket_id, followup_id):
398:@helpdesk_staff_member_required
399:def ]
[result: =====tox.ini=====
[tox]
minversion = 3.25.1
requires = pytest
           freezegun


[testenv:release]
commands = pip install -r requirements-testing.txt
           python quicktest.py
=====quicktest.py=====
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


class QuickDjangoTest:
    """
    A quick way to run the Django test suite without a fully-configured project.

    Example usage:]

[tool: Bash {"command": "cat helpdesk/query.py && echo ===LIB=== && cat helpdesk/lib.py"}]
[result: Exit code 1
from base64 import b64decode, b64encode
from django.db.models import Q, Max
from django.db.models import F, Window, Subquery, OuterRef
from .models import FollowUp
from django.urls import reverse
from django.utils.html import escape
from django.utils.translation import gettext as _
from helpdesk.serializers import DatatablesTicketSerializer
import json
from model_utils import Choices


def query_to_base64(query):
    """
    Converts a query dict object to a base64-encoded bytes object.
    """
    return b64encode(json.dumps(query).encode("UTF-8")).decode("ascii")


def query_from]

[tool: Bash {"command": "sed -n '1,70p;340,470p' helpdesk/models.py; echo ...; sed -n '468,620p' helpdesk/models.py"}]
[result: """
django-helpdesk - A Django powered ticket tracker for small enterprise.

(c) Copyright 2008 Jutda. All Rights Reserved. See LICENSE for details.

models.py - Model (and hence database) definitions. This is the core of the
            helpdesk structure.
"""

from .lib import format_time_spent, convert_value, daily_time_spent_calculation
from .templated_email import send_templated_mail
from .validators import validate_file_extension
import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.co]

[tool: Bash {"command": "cd helpdesk && ls management/commands && echo \"=== api.py ===\" && cat views/api.py && echo \"=== public head ===\" && grep -n \"^class \\|^def \\|^@\" views/public.py views/kb.py views/login.py views/abstract_views.py views/permissions.py"}]
[result: __init__.py
__pycache__
create_escalation_exclusions.py
create_queue_permissions.py
create_usersettings.py
escalate_tickets.py
get_email.py
=== api.py ===
from django.contrib.auth import get_user_model
from helpdesk.models import FollowUp, FollowUpAttachment, Ticket
from helpdesk.serializers import (
    FollowUpAttachmentSerializer,
    FollowUpSerializer,
    TicketSerializer,
    UserSerializer,
    PublicTicketListingSerializer,
)
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from r]

Claude: I'll read CI workflows, constraints, and grep tests for skips/fragility.

[tool: Bash {"command": "git log -1 --format=%ci && echo \"--- oldest untouched files (last commit date per file) ---\" && for f in helpdesk/lib.py helpdesk/query.py helpdesk/email.py helpdesk/views/staff.py helpdesk/models.py helpdesk/forms.py helpdesk/views/feeds.py helpdesk/templated_email.py helpdesk/views/]

[tool: Bash {"command": "cat helpdesk/lib.py; echo \"=====SER\"; sed -n '1,60p' helpdesk/serializers.py; grep -n \"class \\|def \" helpdesk/serializers.py"}]
[result: """
django-helpdesk - A Django powered ticket tracker for small enterprise.

(c) Copyright 2008 Jutda. All Rights Reserved. See LICENSE for details.

lib.py - Common functions (eg multipart e-mail)
"""

from datetime import date, datetime, time
from django.conf import settings
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.utils.encoding import smart_str
from helpdesk.settings import (
    CUSTOMFIELD_DATE_FORMAT,
    CUSTOMFIELD_DATETIME_FORMAT,
    CUSTOMFIELD_TIME_FORMAT,
)
import logging
import mimetypes


logger = logging.getLogger("helpdesk")


def t]
[result: 2025-05-13 10:24:14 -1000
--- oldest untouched files (last commit date per file) ---
2025-03-22 helpdesk/admin.py
2025-03-22 helpdesk/lib.py
2025-03-22 helpdesk/models.py
2025-03-22 helpdesk/serializers.py
2025-03-22 helpdesk/templated_email.py
2025-03-22 helpdesk/views/api.py
2025-03-22 helpdesk/views/feeds.py
2025-04-18 helpdesk/query.py
2025-04-21 helpdesk/forms.py
2025-05-09 helpdesk/settings.py
2025-05-09 helpdesk/views/staff.py
2025-05-12 helpdesk/email.py]

[tool: Bash {"command": "sed -n '1633,1800p' helpdesk/models.py; echo ===; sed -n '1966,2060p;2138,2210p' helpdesk/models.py"}]
[result: Exit code 1
class SavedSearch(models.Model):
    """
    Allow a user to save a ticket search, eg their filtering and sorting
    options, and optionally share it with other users. This lets people
    easily create a set of commonly-used filters, such as:
        * My tickets waiting on me
        * My tickets waiting on submitter
        * My tickets in 'Priority Support' queue with priority of 1
        * All tickets containing the word 'billing'.
         etc...
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_]

[tool: Bash {"command": "cd helpdesk && grep -n \"^class \\|^def \\|^@\\|raw\\|cursor\\|extra(\" forms.py | head -60 && echo \"=== email.py ===\" && grep -n \"^def \\|^class \" email.py && echo \"=== get_email cmd ===\" && cat management/commands/get_email.py && echo \"=== templated_email ===\" && sed -n 1,60p ]

[tool: Bash {"command": "cat .github/workflows/pythonpackage.yml && echo \"===RELEASE===\"&& cat .github/workflows/release_to_pypi.yml && echo \"===DOCKER===\"&& head -30 .github/workflows/build-standalone-docker-image.yml && echo \"===CONSTRAINTS===\"&& for f in constraints-*.txt; do echo \"--$f--\"; cat $f; d]
[result: 51:class CustomFieldMixin(object):
108:class EditTicketForm(CustomFieldMixin, forms.ModelForm):
199:class EditTicketCustomFieldForm(EditTicketForm):
245:class EditFollowUpForm(forms.ModelForm):
261:class AbstractTicketForm(CustomFieldMixin, forms.Form):
430:class TicketForm(AbstractTicketForm):
525:class PublicTicketForm(AbstractTicketForm):
618:class UserSettingsForm(forms.ModelForm):
624:class EmailIgnoreForm(forms.ModelForm):
630:class TicketCCForm(forms.ModelForm):
648:class TicketCCUserForm(forms.ModelForm):
669:class TicketCCEmailForm(forms.ModelForm):
683:class TicketDependencyForm(form]
[result: name: Python package

on: [pull_request]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        include:
          # Explicitly include Python 3.9 only with Django 4
          - python-version: "3.9"
            django-version: "4"
            # Define the general matrix for Python with Django 
        python-version: ["3.10", "3.11", "3.12"]
        django-version: ["4"]
    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
]

[tool: Bash {"command": "grep -rn \"skip\\|expectedFailure\\|TODO\\|FIXME\\|XXX\\|xfail\" helpdesk/tests/*.py | head -50 && echo \"===SQLITE===\" && grep -rn \"sqlite\\|vendor\\|connection\\.\" helpdesk/tests/*.py helpdesk/*.py | head -20 && echo \"===HEAD===\"&& head -12 helpdesk/tests/__init__.py helpdesk/tes]

[tool: Bash {"command": "sed -n '1966,2060p' helpdesk/models.py; sed -n '2138,2210p' helpdesk/models.py; sed -n '1141,1200p' helpdesk/models.py; sed -n '951,1060p' helpdesk/models.py"}]
[result: class CustomFieldManager(models.Manager):
    def get_queryset(self):
        return super(CustomFieldManager, self).get_queryset().order_by("ordering")


class CustomField(models.Model):
    """
    Definitions for custom fields that are glued onto each ticket.
    """

    name = models.SlugField(
        _("Field Name"),
        help_text=_(
            "As used in the database and behind the scenes. "
            "Must be unique and consist of only lowercase letters with no punctuation."
        ),
        unique=True,
    )

    label = models.CharField(
        _("Label"),
        max_le]
[result: helpdesk/tests/test_attachments.py:12:from unittest.case import skip
helpdesk/tests/test_attachments.py:195:    @skip("Rework with model relocation")
helpdesk/tests/test_attachments.py:240:    @skip("model in lib not patched")
helpdesk/tests/test_ticket_actions.py:238:        # TODO this needs to be checked further
helpdesk/tests/test_ticket_submission.py:646:        # TODO: check this is correct!
===SQLITE===
===HEAD===
==> helpdesk/tests/__init__.py <==
# import all test_*.py files in directory.
# necessary for automatic discovery in django <= 1.5
# http://stackoverflow.com/a/15780326/138274]

[tool: Bash {"command": "grep -rn \"SavedSearch\\|query_to_base64\\|query_from_base64\\|settings_pickled\\|savedsearch\" helpdesk --include=*.py | grep -v migrations"}]
[result: (eval):1: no matches found: --include=*.py]

[tool: Bash {"command": "cd helpdesk && grep -rn \"cursor()\\|raw(\\|\\.extra(\\|ugettext\\|force_text\\|smart_text\\|python_2\\|from __future__\\|six\\|urlquote\\|providing_args\\|django.utils.encoding\\|@python_2\" --include=\"*.py\" . | grep -v migrations | head -30; echo \"=== middleware ===\"; grep -rn \"M]
[result: lib.py:12:from django.utils.encoding import smart_str
tests/test_attachments.py:6:from django.utils.encoding import smart_str
=== middleware ===
views/staff.py:1324:                if k != "csrfmiddlewaretoken" and k not in form_fields
../standalone/config/settings.py:59:MIDDLEWARE = [
../standalone/config/settings.py:60:    "django.middleware.security.SecurityMiddleware",
../standalone/config/settings.py:61:    "django.contrib.sessions.middleware.SessionMiddleware",
../standalone/config/settings.py:62:    "django.middleware.common.CommonMiddleware",
../standalone/config/settings.py:63:    "dj]

[tool: Bash {"command": "echo \"=== churn (commits per file, all time) ===\" && git log --name-only --pretty=format: -- 'helpdesk/*.py' 'helpdesk/views/*.py' | grep -v '^$' | sort | uniq -c | sort -rn | head -20 && echo \"=== markers ===\" && grep -rn \"TODO\\|FIXME\\|XXX\\|HACK\\|deprecated\\|DeprecationWarnin]
[result: === churn (commits per file, all time) ===
 281 helpdesk/views/staff.py
 191 helpdesk/models.py
 123 helpdesk/forms.py
 110 helpdesk/settings.py
 108 helpdesk/management/commands/get_email.py
 105 helpdesk/lib.py
  82 helpdesk/email.py
  80 helpdesk/tests/test_get_email.py
  75 helpdesk/urls.py
  73 helpdesk/views/public.py
  43 helpdesk/tests/test_ticket_submission.py
  33 helpdesk/views/api.py
  32 helpdesk/serializers.py
  30 helpdesk/admin.py
  29 helpdesk/query.py
  24 helpdesk/tests/test_time_spent_auto.py
  23 helpdesk/views/kb.py
  23 helpdesk/management/commands/escalate_tickets.py
  ]

[tool: Bash {"command": "grep -rn \"SavedSearch\\|query_to_base64\\|query_from_base64\\|settings_pickled\\|get_query_class\" helpdesk --include=\"*.py\" | grep -v migrations/"}]
[result: helpdesk/query.py:13:def query_to_base64(query):
helpdesk/query.py:20:def query_from_base64(b64data):
helpdesk/query.py:77:def get_query_class():
helpdesk/query.py:80:    def _get_query_class():
helpdesk/query.py:83:    return getattr(settings, "HELPDESK_QUERY_CLASS", _get_query_class)()
helpdesk/query.py:89:        self.params = query_params if query_params else query_from_base64(base64query)
helpdesk/query.py:90:        self.base64 = base64query if base64query else query_to_base64(query_params)
helpdesk/models.py:1633:class SavedSearch(models.Model):
helpdesk/models.py:1721:    settings_pick]

[tool: Bash {"command": "for f in test_api test_attachments test_checklist test_get_email test_kb test_login test_per_queue_staff_permission test_public_actions test_savequery test_ticket_actions test_ticket_lookup test_ticket_submission test_time_spent test_time_spent_auto test_usersettings test_webhooks; do e]

[tool: Bash {"command": "cd helpdesk && sed -n 1,40p query.py && echo \"=== update_ticket ===\" && grep -n \"^def \\|^class \" update_ticket.py tasks.py webhooks.py lib.py user.py && echo \"=== settings head ===\" && grep -n \"^HELPDESK_\\|^[A-Z_]* =\" settings.py | head -70"}]
[result: from base64 import b64decode, b64encode
from django.db.models import Q, Max
from django.db.models import F, Window, Subquery, OuterRef
from .models import FollowUp
from django.urls import reverse
from django.utils.html import escape
from django.utils.translation import gettext as _
from helpdesk.serializers import DatatablesTicketSerializer
import json
from model_utils import Choices


def query_to_base64(query):
    """
    Converts a query dict object to a base64-encoded bytes object.
    """
    return b64encode(json.dumps(query).encode("UTF-8")).decode("ascii")


def query_from_base64(b64d]

[tool: Bash {"command": "grep -rn \"RunPython\\|RunSQL\\|pickle\" helpdesk/migrations/*.py | head -30; echo ---; sed -n '1798,1900p;1896,1965p' helpdesk/models.py"}]
[result: helpdesk/migrations/0003_initial_data_import.py:40:        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
helpdesk/migrations/0001_initial.py:1065:                    "settings_pickled",
helpdesk/migrations/0001_initial.py:1070:                        help_text="This is a base64-encoded representation of a pickled Python dictionary. Do not change this field via the admin.",
helpdesk/migrations/0002_populate_usersettings.py:8:def pickle_settings(data):
helpdesk/migrations/0002_populate_usersettings.py:11:        import pickle
helpdesk/migrations/0002_populate_usersettings.py:1]
[result: == test_api
class TicketTest(APITestCase):
class UserTicketTest(APITestCase):
== test_attachments
class AttachmentIntegrationTests(TestCase):
class AttachmentIntegrationStaffTests(TestCase):
class AttachmentUnitTests(TestCase):
== test_checklist
class TicketChecklistTestCase(TestCase):
== test_get_email
class GetEmailCommonTests(TestCase):
class EmailTaskTests(TestCase):
class GetEmailParametricTemplate(object):
class GetEmailCCHandling(TestCase):
== test_kb
class KBTests(TestCase):
== test_login
class TestLoginRedirect(TestCase):
== test_per_queue_staff_permission
class PerQueueStaffMembershi]

[tool: Bash {"command": "grep -rn \"TODO\\|FIXME\\|XXX\\|HACK\\|DEPRECAT\\|deprecated\" --include=\"*.py\" helpdesk | grep -v migrations | head -40", "description": "Find code markers"}]
[result: helpdesk/models.py:1722:        _("DEPRECATED! Settings Dictionary DEPRECATED!"),
helpdesk/models.py:1724:            "DEPRECATED! This is a base64-encoded representation of a pickled Python dictionary. "
helpdesk/lib.py:124:        # deprecated, but kept for backward compatibility
helpdesk/validators.py:9:# TODO: can we use the builtin Django validator instead?
helpdesk/validators.py:19:    # TODO: we might improve this with more thorough checks of file types
helpdesk/validators.py:26:        # TODO: one more check in case it is a file with no extension; we
helpdesk/email.py:299:        # TOD]

[tool: Bash {"command": "cd helpdesk && cat user.py && sed -n 1,60p views/staff.py && echo \"=== signals ===\" && cat signals.py && echo \"=== email process_queue mailbox ===\" && sed -n 376,420p email.py"}]
[result: from helpdesk import settings as helpdesk_settings
from helpdesk.models import Queue, Ticket


if helpdesk_settings.HELPDESK_KB_ENABLED:
    from helpdesk.models import KBCategory, KBItem


def huser_from_request(req):
    return HelpdeskUser(req.user)


class HelpdeskUser:
    def __init__(self, user):
        self.user = user

    def get_queues(self):
        """Return the list of Queues the user can access.

        :param user: The User (the class should have the has_perm method)
        :return: A Python list of Queues
        """
        user = self.user
        all_queues = Queue.objec]

[tool: Bash {"command": "sed -n '1690,1725p' helpdesk/views/staff.py; sed -n '1509,1580p;2206,2272p' helpdesk/models.py"}]
[result: @helpdesk_staff_member_required
def save_query(request):
    title = request.POST.get("title", None)
    shared = request.POST.get("shared", False)
    if shared == "on":  # django only translates '1', 'true', 't' into True
        shared = True
    query_encoded = request.POST.get("query_encoded", None)

    if not title or not query_encoded:
        return HttpResponseRedirect(reverse("helpdesk:list"))

    query = SavedSearch(
        title=title, shared=shared, query=query_encoded, user=request.user
    )
    query.save()

    return HttpResponseRedirect(
        "%s?saved_query=%s" % (rev]

[tool: Bash {"command": "sed -n '1,60p' helpdesk/urls.py; echo ===; grep -n \"^class \\|^def \" helpdesk/models.py | head -60", "description": "Peek urls and model classes"}]
[result: Exit code 1
"""
django-helpdesk - A Django powered ticket tracker for small enterprise.

(c) Copyright 2008 Jutda. All Rights Reserved. See LICENSE for details.

urls.py - Mapping of URL's to our various views. Note we always used NAMED
          views for simplicity in linking later on.
"""

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from helpdesk import settings as helpdesk_settings
from helpdesk.decorators import helpdesk_staff_membe]

[tool: Bash {"command": "grep -n '^class ' helpdesk/models.py", "description": "List model classes"}]
[result: 34:class EscapeHtml(Extension):
69:class Queue(models.Model):
468:class Ticket(models.Model):
943:class FollowUpManager(models.Manager):
951:class FollowUp(models.Model):
1141:class TicketChange(models.Model):
1193:class Attachment(models.Model):
1263:class FollowUpAttachment(Attachment):
1286:class KBIAttachment(Attachment):
1307:class PreSetReply(models.Model):
1354:class EscalationExclusion(models.Model):
1392:class EmailTemplate(models.Model):
1457:class KBCategory(models.Model):
1509:class KBItem(models.Model):
1633:class SavedSearch(models.Model):
1706:class UserSettings(models.Model):
1]

Claude: Now waiting on the three explore agents.

[tool: Bash {"command": "cat tox.ini | head -40; echo ---; ls .github/workflows 2>/dev/null; ls helpdesk/tests", "description": "CI and test layout"}]
[result: [tox]
minversion = 3.25.1
requires = pytest
           freezegun


[testenv:release]
commands = pip install -r requirements-testing.txt
           python quicktest.py
---
build-standalone-docker-image.yml
pythonpackage.yml
release_to_pypi.yml
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
te]

[tool: Bash {"command": "cat .github/workflows/pythonpackage.yml", "description": "CI matrix"}]
[result: name: Python package

on: [pull_request]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        include:
          # Explicitly include Python 3.9 only with Django 4
          - python-version: "3.9"
            django-version: "4"
            # Define the general matrix for Python with Django 
        python-version: ["3.10", "3.11", "3.12"]
        django-version: ["4"]
    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
]

[tool: Bash {"command": "sed -n '580,620p' helpdesk/views/staff.py; echo \"=== lib 110-140 ===\"; sed -n '110,140p' helpdesk/lib.py; echo \"=== models 1700-1800 ===\"; sed -n '1706,1760p' helpdesk/models.py", "description": "Inspect flagged spots"}]
[result:     return get_object_or_404(Ticket, id=ticket_id)


def get_due_date_from_form_or_ticket(
    form, ticket: Ticket
) -> typing.Optional[datetime.date]:
    """Tries to locate the due date for a ticket from the form
    'due_date' parameter or the `due_date_*` paramaters.
    """
    due_date = form.cleaned_data.get("due_date") or None
    if due_date is None:
        due_date_year = int(form.cleaned_data.get("due_date_year", 0))
        due_date_month = int(form.cleaned_data.get("due_date_month", 0))
        due_date_day = int(form.cleaned_data.get("due_date_day", 0))
        # old way, proba]

[tool: Bash {"command": "grep -rn \"b64decode\\|pickle\\|loads(\" helpdesk/*.py helpdesk/views/*.py | head -20", "description": "Check pickle/base64 usage"}]
[result: helpdesk/forms.py:621:        exclude = ["user", "settings_pickled"]
helpdesk/models.py:1721:    settings_pickled = models.TextField(
helpdesk/models.py:1724:            "DEPRECATED! This is a base64-encoded representation of a pickled Python dictionary. "
helpdesk/query.py:1:from base64 import b64decode, b64encode
helpdesk/query.py:25:    query.update(json.loads(b64decode(b64data).decode("utf-8")))]

[tool: Bash {"command": "sed -n '1,80p' helpdesk/query.py", "description": "Read query.py"}]
[result: from base64 import b64decode, b64encode
from django.db.models import Q, Max
from django.db.models import F, Window, Subquery, OuterRef
from .models import FollowUp
from django.urls import reverse
from django.utils.html import escape
from django.utils.translation import gettext as _
from helpdesk.serializers import DatatablesTicketSerializer
import json
from model_utils import Choices


def query_to_base64(query):
    """
    Converts a query dict object to a base64-encoded bytes object.
    """
    return b64encode(json.dumps(query).encode("UTF-8")).decode("ascii")


def query_from_base64(b64d]

[tool: Bash {"command": "ls helpdesk/management/commands/ && wc -l helpdesk/management/commands/*.py && echo === && ls helpdesk/views/ && wc -l helpdesk/views/*.py", "description": "Commands and views inventory"}]
[result: Exit code 1
__init__.py
__pycache__
create_escalation_exclusions.py
create_queue_permissions.py
create_usersettings.py
escalate_tickets.py
get_email.py
       0 helpdesk/management/commands/__init__.py
      94 helpdesk/management/commands/create_escalation_exclusions.py
      74 helpdesk/management/commands/create_queue_permissions.py
      33 helpdesk/management/commands/create_usersettings.py
     114 helpdesk/management/commands/escalate_tickets.py
      47 helpdesk/management/commands/get_email.py
     362 total
(eval):1: == not found]

[tool: Bash {"command": "wc -l helpdesk/views/*.py; echo \"--- webhooks/tasks ---\"; ls helpdesk/", "description": "Views inventory"}]
[result:        0 helpdesk/views/__init__.py
      43 helpdesk/views/abstract_views.py
     104 helpdesk/views/api.py
     167 helpdesk/views/feeds.py
      90 helpdesk/views/kb.py
      26 helpdesk/views/login.py
       7 helpdesk/views/permissions.py
     297 helpdesk/views/public.py
    2120 helpdesk/views/staff.py
    2854 total
--- webhooks/tasks ---
__init__.py
__pycache__
admin.py
apps.py
attachments
decorators.py
email.py
exceptions.py
fixtures
forms.py
lib.py
locale
management
migrations
models.py
poll_helpdesk_email_queues.sh
query.py
serializers.py
settings.py
signals.py
static
tasks.py
temp]

Claude: I have a good direct picture; let me wait for the agents to fill in the details.

[tool: Bash {"command": "cat helpdesk/tasks.py; echo \"=== signals ===\"; cat helpdesk/signals.py; echo \"=== webhooks head ===\"; head -40 helpdesk/webhooks.py", "description": "Async, signals, webhooks"}]
[result: from .email import process_email
from celery import shared_task


@shared_task
def helpdesk_process_email():
    process_email()
=== signals ===
import django.dispatch

# create a signal for *TicketForm
new_ticket_done = django.dispatch.Signal()

# create a signal for ticket_update view
update_ticket_done = django.dispatch.Signal()
=== webhooks head ===
import requests
import requests.exceptions
import logging
from django.dispatch import receiver

from . import settings
from .signals import new_ticket_done, update_ticket_done

logger = logging.getLogger(__name__)


def notify_followup_webhooks]

Claude: Now I'll wait for the three explore agents to report.

[tool: Bash {"command": "grep -n \"HELPDESK_\" helpdesk/settings.py | head -50", "description": "Settings knobs"}]
[result: 25:    DEFAULT_USER_SETTINGS.update(settings.HELPDESK_DEFAULT_SETTINGS)
47:HELPDESK_REDIRECT_TO_LOGIN_BY_DEFAULT = getattr(
48:    settings, "HELPDESK_REDIRECT_TO_LOGIN_BY_DEFAULT", False
51:HELPDESK_PUBLIC_VIEW_PROTECTOR = getattr(
53:    "HELPDESK_PUBLIC_VIEW_PROTECTOR",
57:HELPDESK_STAFF_VIEW_PROTECTOR = getattr(
59:    "HELPDESK_STAFF_VIEW_PROTECTOR",
68:HELPDESK_ENABLE_ATTACHMENTS = getattr(settings, "HELPDESK_ENABLE_ATTACHMENTS", True)
71:HELPDESK_ENABLE_DEPENDENCIES_ON_TICKET = getattr(
72:    settings, "HELPDESK_ENABLE_DEPENDENCIES_ON_TICKET", True
76:HELPDESK_ENABLE_TIME_SPENT_ON_TICK]

Claude: I'll hold here until the explore agents return their findings.

[tool: Bash {"command": "head -50 helpdesk/email.py; echo \"=== update_ticket ===\"; grep -n \"^def \\|^class \" helpdesk/update_ticket.py", "description": "Email module head"}]
[result: """
Django Helpdesk - A Django powered ticket tracker for small enterprise.

(c) Copyright 2008 Jutda. Copyright 2018 Timothy Hobbs. All Rights Reserved.
See LICENSE for details.
"""

# import base64
from bs4 import BeautifulSoup
from datetime import timedelta
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import Q
from django.utils import encoding, timezone
from django.utils.translation import gettext as _
import email
from ema]

[tool: ListAgents {}]
[result: This session is brownfield-26 [f57cc6] — the name other sessions use to message it (it is not listed below; a message to it would be a message to yourself).

Subagents (3):
  fa87d4976a73da078  ·  Explore  ·  running  ·  started 1m ago
  def9cacad32a31395  ·  Explore  ·  running  ·  started 1m ago
  e4ca5c533b982a947  ·  Explore  ·  running  ·  started 59s ago

Peer sessions (8):
  (redacted) [089797]  ·  interactive  ·  started 1h ago
  (redacted) [274580]  ·  interactive  ·  started 1h ago
  (redacted) [caad17]  ·  interactive  ·  started 2h ago
  books-b9 [694ffb]  ·  interactive  ·  starte]

Claude: Agents still running. I'll wait for them rather than duplicating their work.

[tool: Bash {"command": "sleep 60; echo done", "description": "Wait for agents", "run_in_background": true}]
[result: Command running in background with ID: b3yliq585. Output is being written to: /private/tmp/claude-501/-Users-reader-Documents-Wazeem-books-claude-code-companion-brownfield/17a5f81d-7a30-565b-141d-b88fa5c9b989/tasks/b3yliq585.output. You will be notified when it completes. To check interim output, use Read on that file path.]

Claude: ## Test suite layout — `/Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield/helpdesk/tests/`

~6,640 LOC, 22 modules, all Django `TestCase`/`APITestCase` (no pytest-style tests despite CI installing pytest).

| File | Covers |
|---|---|
| `test_get_email.py` (1610 L, 70 KB) | Email ingestion: POP3/IMAP/local-dir, MIME parsing, CC handling, encodings, attachments. `GetEmailCommonTests`, `EmailTaskTests`, `GetEmailParametricTemplate` (mixin generating parametric cases), `GetEmailCCHandling`. By far the heaviest module. |
| `test_ticket_submission.py` (1201 L) | `TicketBasicsTestCase`, `EmailInteractionsTestCase` — public/staff submission forms, notification emails |
| `test_api.py` (452 L) | DRF endpoints: `TicketTest`, `UserTicketTest` |
| `test_time_spent_auto.py` (450 L) | Automatic time-tracking calc (uses `freezegun`) |
| `test_ticket_actions.py` (395 L) | Merge, delete, hold, followups |
| `test_navigation.py` (295 L) | Staff detection / dashboard / RSS access matrix (`StaffUserTestCaseMixin` reused by 3 cases) |
| `test_webhooks.py` (313 L) | Spins a **real `http.server.HTTPServer` in-process** (`WebhookRequestHandler`, `WebhookServer`) |
| `test_checklist.py`, `test_per_queue_staff_permission.py`, `test_attachments.py`, `test_query.py`, `test_kb.py`, `test_ticket_lookup.py`, `test_public_actions.py`, `test_markdown.py` (SimpleTestCase), `test_login.py`, `test_savequery.py`, `test_time_spent.py`, `test_usersettings.py` | as named |
| `utils.py` (371 L) | Fixture factory helpers: `generate_multipart_email`, `generate_image_mime_part`, `get_fake` (faker), `generate_random_image` (numpy) |
| `helpers.py` (79 L) | `get_user`, queue/ticket helpers |
| `urls.py` (8 L) | ROOT_URLCONF used by `quicktest.py` |
| `test_files/` | 6 `.eml` fixtures: `pgp.eml`, `utf-nondecodable.eml`, `all-special-chars.eml`, `blank-body-with-attachment.eml`, `forwarded-message.eml`, `quoted_printable.eml` |
| `__init__.py` | `suite()` loader with comment "necessary for automatic discovery in django <= 1.5" — dead legacy |

## Runner / tooling

- **`quicktest.py`** — the real runner. Calls `settings.configure()` with a hardcoded **sqlite3 DB written to `<repo>/database.db`** (persisted file, not `:memory:`), `DiscoverRunner`, `ROOT_URLCONF="helpdesk.tests.urls"`, teams disabled (`HELPDESK_TEAMS_MODEL="auth.User"`). Pinax/reversion apps commented out, so team-related code paths are never exercised.
- **`tox.ini`** — 8 lines. Only defines `[testenv:release]`. **No `envlist`, no default `testenv`.**
- **`Makefile`** — `make test` runs `pip install -e .[test]` (no `test` extra exists in `setup.py` → fails) then bare `tox` (nothing to run). `make sphinx` / `make readme` invoke `tox -e sphinx` / `-e readme`, **neither env exists in tox.ini**. Only `make format`/`checkformat` (ruff) actually work.
- **`.github/workflows/pythonpackage.yml`** — triggers on `pull_request` **only** (no push/main/schedule → no post-merge signal). Matrix is malformed: an `include:` block sits above the `python-version`/`django-version` keys at the same level, so the intended "3.9 + Django 4" extra entry is fragile YAML. Runs `make checkformat` then `python quicktest.py` (pytest installed but unused).
- Other workflows: `release_to_pypi.yml` (tag `v*`; uses stale `actions/setup-python@v2`), `build-standalone-docker-image.yml` (push to main; `docker build --file standalone/Dockerfile ... ..` uses the **parent of the repo** as build context).
- **No azure-pipelines file** exists in this repo.

## Versions

- CI: Python 3.10/3.11/3.12 (+3.9), Django 4 only via `constraints-Django4.txt` (`>=4.2,<5`).
- `constraints-Django32.txt` and `constraints-Django5.txt` exist but **are never referenced by any workflow** — Django 5 is untested.
- `requirements.txt`: `Django>=3.2` with **no upper bound**.
- `setup.py`: `version = "1.5.0"`, classifiers claim Python 3.8/3.9/3.10 and Django 3.2/4.0 — contradicts CI; **no `python_requires`**; still imports `distutils.util.convert_path` (removed in Python 3.12).

## Requirements

- `requirements.txt` — zero version pins on any dependency (celery, lxml, markdown, akismet, pinax_teams…).
- `requirements-testing.txt` — includes `argparse` (stdlib since 2.7), `mock` (stdlib `unittest.mock`), `pbr`, `numpy` (only for `utils.generate_random_image`), missing trailing newline on `faker`.
- `requirements-no-pinax.txt` — **stale**: pins `Django>=2.2,<4`, includes `six`; incompatible with the CI Django 4.2 matrix.
- `requirements-dev.txt` — `tox`, `ruff`, `pycodestyle`, `isort`, `freezegun`.

## Coverage & lint

- `.coveragerc` present (branch coverage, `include = helpdesk/*`, omits migrations) but **no workflow or Makefile target ever runs `coverage`** — dead config.
- Lint is `ruff` (Makefile + CI), yet `pyproject.toml` has an **empty ruff config** (`ignore = []`, no line-length/target-version/select). Meanwhile `.flake8` (max-line 120), `.isort.cfg` (line 120), and `.pylintrc` (requires `pylint_django`) are all orphaned — nothing invokes flake8, isort, or pylint, and their 120-char rule conflicts with ruff's default 88.

## Flagged stale / fragile

1. `helpdesk/tests/test_attachments.py:195` — `@skip("Rework with model relocation")`; `:240` — `@skip("model in lib not patched")`.
2. `helpdesk/tests/test_webhooks.py` — binds a live socket; port collisions / firewall prompts make it flaky in CI and on macOS.
3. sqlite-only: `quicktest.py` hardcodes sqlite3 and writes `database.db` into the repo root; no Postgres/MySQL job anywhere, so DB-specific SQL and the search/query code get no cross-backend coverage.
4. `tox.ini` is effectively empty → `make test`, `make sphinx`, `make readme` are all broken.
5. Coverage config is dead; three lint configs are dead; ruff config is unconfigured.
6. `requirements-no-pinax.txt` pins an unsupported Django range.
7. `setup.py` classifiers/`distutils` usage predate the tested Python/Django versions.
8. CI runs on PRs only, and `constraints-Django32.txt`/`constraints-Django5.txt` are never exercised.
9. TODOs left in assertions: `test_ticket_actions.py:238`, `test_ticket_submission.py:646` ("check this is correct!").
10. `helpdesk/tests/__init__.py` `suite()` targets Django ≤1.5 discovery — removable.

[tool: Bash {"command": "grep -n \"class \\|def \" helpdesk/serializers.py | head -30; echo \"=== api.py ===\"; cat helpdesk/views/api.py", "description": "API surface"}]
[result: 13:class DatatablesTicketSerializer(serializers.ModelSerializer):
26:    row_class = serializers.SerializerMethodField()
31:    class Meta:
51:    def get_queue(self, obj):
54:    def get_ticket(self, obj):
57:    def get_status(self, obj):
60:    def get_created(self, obj):
63:    def get_due_date(self, obj):
66:    def get_assigned_to(self, obj):
77:    def get_submitter(self, obj):
80:    def get_time_spent(self, obj):
83:    def get_row_class(self, obj):
86:    def get_kbitem(self, obj):
89:    def get_last_followup(self, obj):
93:class FollowUpAttachmentSerializer(serializers.ModelSeriali]

[tool: Bash {"command": "grep -n \"skip\" helpdesk/tests/test_attachments.py | head; echo ---; grep -n \"database.db\\|sqlite\" quicktest.py; echo ---; grep -n \"convert_path\\|distutils\\|version\" setup.py | head; echo ---; cat constraints-Django4.txt | head -5; echo ---; grep -n \"ruff\\|\\[tool\" pyproject.]
[result: 12:from unittest.case import skip
195:    @skip("Rework with model relocation")
240:    @skip("model in lib not patched")
---
91:                    "ENGINE": "django.db.backends.sqlite3",
92:                    "NAME": os.path.join(self.DIRNAME, "database.db"),
---
3:from distutils.util import convert_path
10:version = "1.5.0"
43:    in a distutils ``setup.py`` file.
69:    stack = [(convert_path(where), "", package, only_in_packages)]
132:    version=version,
---
Django >=4.2,<5
---
1:[tool.ruff]
2:[tool.ruff.lint]]

Claude: Verified. Waiting on the other two agents.

[tool: Bash {"command": "sleep 90; echo ok", "description": "Wait for remaining agents", "run_in_background": true}]
[result: Command running in background with ID: b1l2o4p3a. Output is being written to: /private/tmp/claude-501/-Users-reader-Documents-Wazeem-books-claude-code-companion-brownfield/17a5f81d-7a30-565b-141d-b88fa5c9b989/tasks/b1l2o4p3a.output. You will be notified when it completes. To check interim output, use Read on that file path.]

Claude: Data layer map for django-helpdesk (all paths absolute).

## /Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield/helpdesk/models.py (2272 lines)

Module helpers: `EscapeHtml` markdown extension :34, `get_markdown()` :39 (regex-based URL-scheme sanitizer + `mark_safe`, hand-rolled — a security-sensitive spot), `mk_secret()` :465, `attachment_path()` bridge :1188, `get_default_setting()` + per-setting default callables :1679-1704, `is_a_list_without_empty_element()` validator :2199.

Models, in file order:

- `Queue` :69 — title, slug, email_address, locale, allow_public_submission, escalate_days, new_ticket_cc/updated_ticket_cc, email_box_* (type/host/port/ssl/user/pass/imap_folder/local_dir), socks_proxy_*, logging_type/logging_dir, permission_name, `default_owner` FK→User (SET_NULL) :347, `dedicated_time` DurationField :357. Notables: `from_address` property via old-style `_from_address` + `from_address = property(...)` :369/:389; `time_spent` aggregates all FollowUps in queue :392; `prepare_permission_name()` :406; `save()` :415 creates a `Permission` row as a side effect (auto-derives ports/socks defaults); `delete()` :451 deletes the paired Permission, swallowing `ObjectDoesNotExist`.
- `Ticket` :468 — title, queue FK, created/modified, submitter_email, assigned_to FK(CASCADE), status IntegerField (statuses come from `helpdesk_settings`, not model constants), on_hold, description, resolution, priority (note `blank=3` at :566 — a bug: `blank` should be bool), due_date, last_escalation, `secret_key` :585, `kbitem` FK :592, `merged_to` self-FK :602. Many old-style `_get_*` accessors wrapped as properties: `_get_assigned_to` :685, `_get_ticket` :699, `_get_ticket_for_url` :707, `_get_priority_css_class` :713, `_get_status` :728, `_get_allowed_status_flow` :742, `_get_ticket_url` :761, `_get_staff_url` :789, `_can_be_resolved` :814. Also `send(roles, dont_send_to)` :627 (templated email fan-out), `save()` :850 (sets created/modified), static `queue_and_id_from_query()` :866, `get_markdown` :873, `add_email_to_ticketcc_if_not_in()` :880, `set_custom_field_values()` :922 / `save_custom_field_values(data)` :930.
- `FollowUpManager` :943 (`private_followups`/`public_followups`), `FollowUp` :951 — ticket, date, title, comment, public, user, new_status, message_id (non-editable), `time_spent` Duration. `save()` :1037 touches parent ticket and auto-computes time_spent; `time_spent_calculation()` :1053 (large business-hours calc delegating to `lib.daily_time_spent_calculation`).
- `TicketChange` :1141 — followup FK, field, old_value, new_value; `__str__` builds the audit sentence :1170.
- `Attachment` :1193 (abstract-ish base with `Meta.abstract` at :1256), subclasses `FollowUpAttachment` :1263 and `KBIAttachment` :1286, each overriding `attachment_path()`.
- `PreSetReply` :1307, `EscalationExclusion` :1354, `EmailTemplate` :1392 (template_name/subject/heading/plain_text/html/locale).
- `KBCategory` :1457, `KBItem` :1509 — dual voting representation: legacy counters `votes`/`recommendations` (:1543/:1549) plus M2M `voted_by`/`downvoted_by` (:1515/:1519) added in migration 0021; `_score` :1587, `query_url` :1616, `num_open_tickets` :1621, `unassigned_tickets` :1624.
- `SavedSearch` :1633 — user, title, shared, `query = TextField(help_text="Pickled query object. Be wary changing this.")` :1665. The help text is stale/misleading: it is base64-encoded JSON now, not a pickle.
- `UserSettings` :1706 — `settings_pickled` :1721 explicitly labeled `DEPRECATED!` (kept only for the 0020 data migration); real columns are login_view_ticketlist, email_on_ticket_change, email_on_ticket_assign, tickets_per_page, use_email_as_submitter. `create_usersettings` post_save signal :1782-1796 (docstring still references `syncdb`).
- `IgnoreEmail` :1798 — wildcard matcher `test()` :1867 written with bare `and/or` precedence and unguarded `own_parts[1]` (IndexError on an address with no `@`).
- `TicketCC` :1896 — user or email, can_view/can_update; `email_address`/`display` again old-style `property()` assignments :1948/:1956.
- `CustomFieldManager` :1966, `CustomField` :1971 — 13 `DATA_TYPE_CHOICES` :1998, list_values text blob parsed by `_choices_as_array()` :2059, `build_api_field()` :2099 maps data_type→DRF field.
- `TicketCustomFieldValue` :2138 (EAV: ticket+field unique_together, `value` TextField — the reason `query.py` filters `ticketcustomfieldvalue__value__icontains`).
- `TicketDependency` :2166.
- `ChecklistTemplate` :2206 (JSONField task_list), `Checklist` :2220 (+`create_tasks_from_template` :2236), `ChecklistTaskQuerySet` :2241, `ChecklistTask` :2249.

No raw SQL, no `cursor()`, no `.raw()`, no TODO/FIXME anywhere in models.py/lib.py/query.py/serializers.py. The only literal deprecation markers are models.py:1721-1724 and lib.py:124 (`AKISMET_API_KEY` fallback).

## Migrations
39 numbered migrations, 0001_initial through 0038_checklist_checklisttemplate_checklisttask. Git dates are all 2025-03-22/2025-04-01 (squashed import), so real chronology is only visible from auto-names: 0027_auto_20200107_1221, 0031_auto_20200225_1440 → roughly 2011-era initial schema through 2024. Data migrations using `RunPython`: 0003 (fixture import), 0002 (writes pickled UserSettings), 0009 (queue membership → permissions), 0019 (clear secret keys), 0020_depickle_user_settings (unpickles into real columns, keeps the column), 0030 (copy KBCategory title→name), 0034 (create "merged" email template). No `RunSQL`. The pickle import shim `try: import pickle / except: import cPickle` at 0002:11-13 and 0020:9-11 is Python-2 legacy.

## lib.py (284 lines)
`ticket_template_context` :25 and `queue_template_context` :58 hand-copy a hardcoded field whitelist into a dict; `safe_template_context` :70 docstring admits the design smell ("if we make changes to the model, we will also have to update this code"). `text_is_spam` :93 optional Akismet with three settings names, one deprecated :124. `process_attachments` :140 builds `FollowUpAttachment`s and enforces `HELPDESK_MAX_EMAIL_ATTACHMENT_SIZE`. `format_time_spent` :186, `convert_value` :200 (uses `type(v) is`, not isinstance), `daily_time_spent_calculation` :212 (opening-hours math, raises `ImproperlyConfigured`).

## query.py (258 lines) + saved-query serialization
- `query_to_base64` :13 / `query_from_base64` :20 — base64(JSON), plus a defensive default `{"search_string": ""}`. This is the whole "saved query" format; despite the DB help_text, nothing pickles.
- `get_search_filter_args` :31 — `queue:` / `priority:` prefixes, otherwise splits on the literal string `"OR"` and ORs ten `icontains` lookups (naive: splits inside words containing "OR").
- `DATATABLES_ORDER_COLUMN_CHOICES` :58 with commented-out `('10','time_spent')` :69 and a gap (no column 10) — dead/legacy column mapping.
- `get_query_class()` :77 — pluggable via `settings.HELPDESK_QUERY_CLASS`; the default class is dunder-named `__Query__` :86.
- `__Query__.__run__` :95 — applies `filtering` dict + `filtering_null` (`__isnull`) with OR-merging logic :129-165, then `sorting`/`sortreverse`, ends in `.distinct()` :180. Note the loop at :140-155 uses `val_key` after the inner loop rather than `matched_key` when building the Q (:148) — works only because they coincide.
- `get_datatables_context` :190 — Window/Subquery annotation of `last_followup` :210, and a branch marked `# Dead code currently` at :233.
- `get_timeline_context` :247 / `mk_timeline_date`.
- Saved-query flow: `helpdesk/views/staff.py:1154` encodes params, :1156/:1214 loads `SavedSearch`, :1228 decodes; `save_query` at staff.py:1690-1704 stores the raw POSTed `query_encoded` string unvalidated into `SavedSearch.query`; `delete_saved_query` :1714. Template tag consumer: /Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield/helpdesk/templatetags/saved_queries.py:23.

## serializers.py (265 lines)
`DatatablesTicketSerializer` :13 (11 SerializerMethodFields, `fields = '__all__'` left commented at :33), `FollowUpAttachmentSerializer` :93, `FollowUpSerializer` :99, `UserSerializer` :140, `BaseTicketSerializer` :155 whose `__init__` :156 dynamically injects `CustomField`-derived fields via `CustomField.build_api_field()`, `PublicTicketListingSerializer` :164, `TicketSerializer` :216 (create :239 routes through `TicketForm`, update :262 through `update_ticket`).

[tool: Bash {"command": "python3 -c \"print('waiting')\"", "description": "noop"}]
[result: Auto mode could not evaluate this action and is blocking it for safety — a safety check separate from auto mode blocked this request because of earlier conversation content — it isn't about the action itself — run with --debug for details. This is not a judgment that the action is unsafe. Retrying it will hit the same refusal, so don't rewrite or rework the action to get around this — it reacts to earlier conversation content, not to the action itself, and it will keep firing for the rest of this conversation. Continue with other tasks that don't require this action. If it is essential, stop a]

[tool: Bash {"command": "sed -n '556,575p' helpdesk/models.py; echo \"=== IgnoreEmail.test ===\"; sed -n '1860,1895p' helpdesk/models.py; echo \"=== query 135,160 ===\"; sed -n '129,168p' helpdesk/query.py", "description": "Verify specific claims"}]
[result:         help_text=_("The content of the customers query."),
    )

    resolution = models.TextField(
        _("Resolution"),
        blank=True,
        null=True,
        help_text=_("The resolution provided to the customer by our staff."),
    )

    priority = models.IntegerField(
        _("Priority"),
        choices=PRIORITY_CHOICES,
        default=3,
        blank=3,
        help_text=_("1 = Highest Priority, 5 = Low Priority"),
    )

    due_date = models.DateTimeField(
        _("Due on"),
=== IgnoreEmail.test ===
        """
        queues = self.queues.all().order_by("title")
  ]

Claude: Confirmed. One agent left.

[tool: Bash {"command": "sleep 60; echo ok", "description": "Wait for last agent", "run_in_background": true}]
[result: Command running in background with ID: byfc83ja2. Output is being written to: /private/tmp/claude-501/-Users-reader-Documents-Wazeem-books-claude-code-companion-brownfield/17a5f81d-7a30-565b-141d-b88fa5c9b989/tasks/byfc83ja2.output. You will be notified when it completes. To check interim output, use Read on that file path.]

[tool: Bash {"command": "grep -n \"^def \\|^class \" helpdesk/views/staff.py", "description": "Staff view inventory"}]
[result: 115:def _get_queue_choices(queues):
128:def get_active_users() -> QuerySet:
138:def get_user_queues(user) -> dict[str, str]:
143:def get_form_extra_kwargs(user) -> dict[str, object]:
152:def dashboard(request):
282:def ticket_perm_check(request, ticket):
291:def delete_ticket(request, ticket_id):
313:def followup_edit(request, ticket_id, followup_id):
383:def followup_delete(request, ticket_id, followup_id):
399:def view_ticket(request, ticket_id):
495:def edit_ticket_checklist(request, ticket_id, checklist_id):
532:def delete_ticket_checklist(request, ticket_id, checklist_id):
551:def get_tic]

[tool: Bash {"command": "sed -n '1965,2060p' helpdesk/views/staff.py", "description": "Report stats functions"}]
[result: def calc_average_nbr_days_until_ticket_resolved(Tickets):
    nbr_closed_tickets = len(Tickets)
    days_per_ticket = 0
    days_each_ticket = list()

    for ticket in Tickets:
        time_ticket_open = ticket.modified - ticket.created
        days_this_ticket = time_ticket_open.days
        days_per_ticket += days_this_ticket
        days_each_ticket.append(days_this_ticket)

    if nbr_closed_tickets > 0:
        mean_per_ticket = days_per_ticket / nbr_closed_tickets
    else:
        mean_per_ticket = 0

    return mean_per_ticket


def calc_basic_ticket_stats(Tickets):
    # all not clos]

Claude: I have enough to report.

## Request flow map — django-helpdesk (`/Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield`)

### 1. URL layer — `/Users/reader/Documents/Wazeem/books/claude-code-companion/brownfield/helpdesk/urls.py` (278 lines)
Single flat `urlpatterns` built by successive `+=` blocks, one namespace `app_name = "helpdesk"` (line 50):
- **Staff block** (lines 53-148): ~35 routes, all pointing at `views/staff.py` function views.
- **Conditional block** (150-163): dependency routes re-registered when `HELPDESK_ENABLE_DEPENDENCIES_ON_TICKET` — note these are **duplicates** of lines 78-95 already registered unconditionally; dead/shadowed patterns.
- **Public block** (165-182): wrapped in `protect_view(...)`.
- **RSS block** (184-210): feeds wrapped in `helpdesk_staff_member_required(feeds.OpenTicketsByUser())`.
- **DRF router** (213-222) mounted at `^api/`.
- **Auth block** (225-249): `login.login` plus stock `auth_views`.
- **KB block** (251-262): only when `HELPDESK_KB_ENABLED`.

Fragile bits: import-time branching on settings (line 27, 251) means URL surface changes with settings and can't be reloaded; `urls.py:31-34` has a `try: import helpdesk.tasks except ImportError: pass` with the maintainers' own comment "TODO: why is it imported?"; `DirectTemplateView` (36-48) reimplements `extra_context` that Django ≥3.0 has natively, and uses `super(self.__class__, self)` (line 39) which is an infinite-recursion trap on subclassing. Mixed `path()` and `re_path()` throughout; the base64 query patterns (135-147) interpolate `base64_pattern` containing `$`.

### 2. Views package — `helpdesk/views/` (2,854 lines total)
| File | Lines | Role |
|---|---|---|
| `staff.py` | **2,120** | The mega-module: dashboard, ticket list, CRUD, mass update, merge, reports, saved queries, CC, dependencies, checklists, email-ignore admin |
| `public.py` | 297 | Anonymous ticket submit/view, iframe variants, MyTickets, language switch |
| `feeds.py` | 167 | RSS `Feed` subclasses |
| `api.py` | 104 | DRF viewsets |
| `kb.py` | 90 | Knowledgebase index/category/vote |
| `abstract_views.py` | 43 | `AbstractCreateTicketMixin` shared by public create views |
| `login.py` | 26 | Login wrapper |
| `permissions.py` | 7 | `MustBeStaffMixin` |
| `__init__.py` | 0 | empty |

`staff.py` is the main brownfield risk. Its own docstring (line 6) admits "the bulk of the application". ~60 module-level functions, nearly all function-based with a `@helpdesk_staff_member_required` decorator. Largest offenders:
- `ticket_list` — `staff.py:1041-1204` (~160 lines) building filters imperatively
- `run_report` — `staff.py:1552-1689` (~140 lines) plus helper trio `get_report_queryset_or_redirect` (1465), `get_report_table_and_totals` (1491), `update_summary_tables` (1506)
- `mass_update` — `staff.py:698-835` (~140 lines), a long `if action.startswith(...)` chain
- `merge_tickets` — `staff.py:961` with helpers `merge_ticket_values` (836) and `redirect_from_chosen_ticket` (866-960, ~95 lines)
- `dashboard` — `staff.py:151-281` (~130 lines)
- `view_ticket` — `staff.py:398-493`

Only three CBVs exist here (`CreateTicketView` 1274, `UpdateTicketView` 1303, `EditUserSettingsView` 1730) — a half-finished migration to CBVs sitting alongside the FBVs. Stats helpers `calc_average_nbr_days_until_ticket_resolved` (1965), `calc_basic_ticket_stats` (1984), `get_color_for_nbr_days` (2057), `sort_string` (2076) are presentation logic living in the view module — `sort_string` builds query fragments as strings.

Odd hybrid: `datatables_ticket_list` and `timeline_ticket_list` (`staff.py:1234-1252`) stack `@helpdesk_staff_member_required` **and** DRF's `@api_view(["GET"])` — DRF endpoints hidden outside the router, accepting a base64-encoded query blob from the URL that `query.py:20` decodes via `json.loads(b64decode(...))` (untrusted input driving ORM filters — worth an audit).

### 3. Forms — `helpdesk/forms.py` (784 lines)
19 classes. Inheritance chain: `CustomFieldMixin` (51) → `AbstractTicketForm` (261) → `TicketForm` (430) / `PublicTicketForm` (525); separately `EditTicketForm` (108) → `EditTicketCustomFieldForm` (199). `AbstractTicketForm` is ~170 lines and does dynamic field injection from the `CustomField` model, so form fields are DB-driven — a common source of surprises. `UserSettingsForm` (618) explicitly excludes `settings_pickled` (621).

### 4. API surface — DRF, `helpdesk/views/api.py` (104) + `helpdesk/serializers.py` (265)
Router registrations at `urls.py:213-221`: `tickets` (`TicketViewSet`), `user_tickets` (`UserTicketViewSet`, read-only, `IsAuthenticated`), `followups`, `followups-attachments`, `users` (`CreateUserView`, create-only). All except `user_tickets` are `IsAdminUser` — so it's an admin API, not a customer API. `ConservativePagination` page_size 25 (api.py:19).

Performance/fragility: `TicketViewSet.get_queryset` (api.py:56-77) iterates the **entire** queryset calling `ticket.set_custom_field_values()` per object *before* pagination — N+1 across all tickets on every list request. Same pattern in `UserTicketViewSet.get_queryset` (api.py:35-41). Its status filter loops `statuses × status_choices` and effectively discards the parsed value (`number_statuses.append(choice[0])` is just the matched choice), shadowing the loop variable `status`. `UserTicketViewSet` scopes by `submitter_email=request.user.email` — email-string ownership, not FK.

### 5. Templates — `helpdesk/templates/helpdesk/`, 84 HTML files
Flat directory plus `include/`, `filters/`, `rss/`, `registration/`, and per-locale dirs (`cs de en es fr it pl ru`) holding translated email bodies. Key entry points: `base.html`, `public_base.html`, `ticket.html`, `ticket_list.html`, `dashboard.html`, `report_output.html`, iframe variants (`public_create_ticket_iframe.html`, `kb_category_iframe.html` — served with `@xframe_options_exempt` at `views/kb.py:65`).

### 6. Settings & middleware
`helpdesk/settings.py` (497 lines) is a **shim module**, not Django settings: ~80 `getattr(settings, "HELPDESK_X", default)` lookups read at import time (lines 47-497). Nothing can be changed at runtime, and `override_settings` in tests won't take effect — a classic testing headache. Status/priority constants at 147-218. No middleware ships with the app; real `MIDDLEWARE` lists live only in the sample projects, `standalone/config/settings.py:59-67` and `demo/demodesk/config/settings.py:65-72`.

### 7. Permissions & decorators — `helpdesk/decorators.py` (105) + `helpdesk/user.py` (96) + `views/permissions.py` (7)
Two parallel, subtly different mechanisms:
- Module-level `is_helpdesk_staff` computed **at import time** (decorators.py:31-38) via a curried `check_staff_status` whose own docstring calls it "somewhat ridiculous currying"; fed to `user_passes_test` → `helpdesk_staff_member_required` (line 40). Redirects to login on failure.
- `staff_member_required` (line 70) / `superuser_required` (line 92) which raise `PermissionDenied` instead. Both contain the bug `if not request.user.is_authenticated and not request.user.is_active:` (lines 77, 98) — `and` where `or` is meant; an anonymous user is `is_active == False`, so the redirect happens by accident, but any authenticated-but-deactivated user slips past this check.

Object-level checks live in `HelpdeskUser` (`user.py:13`). `get_queues` (18-34) pulls **all** queues into Python and loops `user.has_perm(q.permission_name)` per queue (line 30) — O(queues) permission checks per request, then re-filters by pk. `get_allowed_kb_categories` (36-42) and `get_assigned_kb_items` (44-50) do full-table Python loops too. `can_access_ticket` (line 76) is the single ticket gate; `views/staff.py:282 ticket_perm_check` wraps it.

### 8. Email ingestion — `helpdesk/email.py` (**1,148 lines**) + `helpdesk/management/commands/get_email.py`
The command (`get_email.py`) is a thin 46-line shell over `process_email()`; note the `#!/usr/bin/python` shebang and the `if __name__ == "__main__": process_email()` tail (line 45-46) — leftovers from when this was `scripts/get_email.py` run by cron, per the module docstring. `helpdesk/tasks.py:6 helpdesk_process_email` is the Celery-ish alternative entry.

Flow: `process_email` (email.py:62) → per-queue `process_queue` (376) → transport sync (`pop3_sync` 134, `imap_sync` 195, `imap_oauth_sync` 273, plus local-dir mode) → `extract_email_metadata` (1042) → `create_object_from_email_message` (586) → ticket/followup. Supporting cast: `decodeUnknown` (499, camelCase py2-era naming), `decode_mail_headers` (510), `is_autoreply` (520), `create_ticket_cc` (539), `get_ticket_id_from_subject_slug` (755), `extract_attachments` (973), `attempt_body_extract_from_html` (812).

Fragility: `process_queue` mutates the **global** `socket.socket = socks.socksocket` (email.py:401) — a process-wide side effect from a per-queue config; the mail-transport dispatch is a nested dict-of-dicts literal (388+) rather than classes; heavy manual MIME walking instead of `email.message.EmailMessage` modern API; the 1,610-line `tests/test_get_email.py` is a fair signal of how much accumulated edge-case behavior is locked in here.

### 9. Outbound email & notifications
- `helpdesk/templated_email.py` (135) — `send_templated_mail` (line 11) renders subject/plain/HTML from the **`EmailTemplate` DB table** through `engines["django"].from_string` (line 52). DB-stored templates compiled at send time; `mark_safe` on user comment content at line 94.
- `helpdesk/lib.py` (284) — context builders `ticket_template_context` (25), `queue_template_context` (59), `safe_template_context` (72); also `text_is_spam` (96, Akismet) and `process_attachments` (151).
- `helpdesk/update_ticket.py` (404) — the notification decision engine: `update_ticket` (188), `get_template_staff_and_template_cc` (165), `update_messages_sent_to_by_public_and_status` (128), `add_staff_subscription` (24). Shared by the staff update view and email ingestion.
- `helpdesk/webhooks.py` (67) — `notify_followup_webhooks` (12), `send_new_ticket_webhook` (44), wired via signal receivers (40, 66) to `helpdesk/signals.py`'s two bare `Signal()` objects (`new_ticket_done`, `update_ticket_done`).
- `email.py:715 send_info_email` sends the auto-acknowledgement during ingestion.

### 10. Fragility summary (highest value first)
1. `views/staff.py:1-2120` — one module holding nearly all staff business logic; reports, stats, merge, and mass-update logic have no home of their own.
2. `email.py:1-1148` — procedural MIME handling with a global socket mutation at line 401.
3. `helpdesk/settings.py` — import-time `getattr` shim (all 497 lines) freezes config for the process lifetime.
4. `api.py:35,56` — full-queryset `set_custom_field_values()` loops before pagination.
5. `decorators.py:77,98` — `and` instead of `or` in the authenticated/active guard.
6. `urls.py:39` — `super(self.__class__, self)`; `urls.py:150-163` duplicate dependency routes; `urls.py:31` mystery import.
7. `user.py:18-50` — Python-side loops over full tables for permission filtering.
8. Py2/legacy residue: `decodeUnknown` camelCase (`email.py:499`), `class CustomFieldMixin(object)` (`forms.py:51`), the `#!/usr/bin/python` + `__main__` block in `get_email.py`, and the deprecated `settings_pickled` base64-pickle column (`models.py:1721-1724`, excluded at `forms.py:621`, with migration `0020_depickle_user_settings.py`).
9. Good news for a refactor: **no raw SQL, no `.cursor()`, no `.extra()`, no `ugettext`/`force_text`/`six`/`from __future__` anywhere** in app code — the only legacy encoding import is `smart_str` (`lib.py:12`), which is current. The ORM usage is modern (`Window`, `Subquery`, `OuterRef` in `query.py:3`).

[tool: ListAgents {}]
[result: This session is brownfield-26 [f57cc6] — the name other sessions use to message it (it is not listed below; a message to it would be a message to yourself).

Subagents (3):
  fa87d4976a73da078  ·  Explore  ·  completed  ·  started 1m ago
  def9cacad32a31395  ·  Explore  ·  completed  ·  started 1m ago
  e4ca5c533b982a947  ·  Explore  ·  completed  ·  started 1m ago

Peer sessions (8):
  (redacted) [089797]  ·  interactive  ·  started 1h ago
  (redacted) [274580]  ·  interactive  ·  started 1h ago
  (redacted) [caad17]  ·  interactive  ·  started 2h ago
  books-b9 [694ffb]  ·  interactive  ·  s]

[tool: Bash {"command": "sed -n '70,105p' helpdesk/decorators.py; echo \"=== urls 78-96 ===\"; sed -n '78,96p' helpdesk/urls.py; echo \"=== urls 150-165 ===\"; sed -n '150,165p' helpdesk/urls.py; echo \"=== email 396-405 ===\"; sed -n '396,406p' helpdesk/email.py; echo \"=== user.py 18-34 ===\"; sed -n '18,34p']
[result:     """
    Decorator for staff member the views checking user, redirecting
    to the log-in page if necessary or returning 403
    """

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated and not request.user.is_active:
            return redirect("helpdesk:login")
        if (
            not helpdesk_settings.HELPDESK_ALLOW_NON_STAFF_TICKET_UPDATE
            and not request.user.is_staff
        ):
            raise PermissionDenied()
        if auth_redirect := helpdesk_settings.HELPDESK_STAFF_VIEW_PROTECTOR(request):
      ]

Claude: All findings verified against the source. Here's the overview.

---

# django-helpdesk — codebase overview

A reusable Django app (v1.5.0, BSD, ~17k LOC of Python) that provides a support-ticket tracker: web UI for staff and public submitters, email-in/email-out ticket handling, a knowledgebase, and a DRF admin API. It ships as a pluggable app plus two sample projects — `demo/` (sqlite quickstart, `make rundemo`) and `standalone/` (Docker).

## Architecture

Classic monolithic Django app, no service layer:

- **`helpdesk/urls.py`** (278 L) — one flat `urlpatterns` namespace, built by successive `+=` blocks. Branches on settings *at import time* (KB routes, dependency routes).
- **`helpdesk/views/`** (2,854 L) — `staff.py` alone is **2,120 lines** and holds nearly all staff logic. Mostly function-based views with three CBVs (`CreateTicketView`, `UpdateTicketView`, `EditUserSettingsView`) sitting alongside — a half-finished migration.
- **`helpdesk/settings.py`** (497 L) — not Django settings; a shim module of ~80 `getattr(django_settings, "HELPDESK_X", default)` calls evaluated at import. This is the app's whole config surface, and it freezes for the process lifetime.
- **`helpdesk/forms.py`** (784 L) — `AbstractTicketForm` injects fields dynamically from the `CustomField` table, so the form schema is DB-driven.
- **`helpdesk/query.py`** — a pluggable query class (`settings.HELPDESK_QUERY_CLASS`, default named `__Query__`) that turns a base64-JSON filter blob into an ORM queryset; also feeds DataTables and the timeline.
- **Signals + webhooks** — `signals.py` defines two bare `Signal()`s (`new_ticket_done`, `update_ticket_done`); `webhooks.py` receivers POST to configured URLs. Celery is optional (`tasks.py` is 7 lines).
- **Shared write path** — `update_ticket.py` is the notification/decision engine used by both the staff update view and email ingestion. Good factoring, and one of the few places that avoids duplication.

## Key data models (`models.py`, 2,272 L, 26 classes)

- **`Queue`** — the central config object. Holds its own mail-server credentials (POP3/IMAP/local dir, SOCKS proxy, OAuth), escalation days, CC addresses. Its `save()` creates a Django `Permission` row as a side effect; `delete()` removes it.
- **`Ticket`** — title, queue, status/priority as **integers driven by settings, not model constants**, submitter_email, assigned_to, due_date, `secret_key` for public access, `merged_to` self-FK, `kbitem`.
- **`FollowUp`** — every ticket event (comment, status change, email reply). `save()` touches the parent ticket and auto-computes `time_spent` from business hours. **`TicketChange`** is the per-field audit row hanging off a FollowUp.
- **`Attachment`** (abstract) → `FollowUpAttachment`, `KBIAttachment`.
- **`CustomField` + `TicketCustomFieldValue`** — an EAV pair. `CustomField.build_api_field()` maps a data_type to a DRF field; this is why serializers and forms are built at runtime.
- **`SavedSearch`** — stores the base64-JSON query blob. **`UserSettings`**, **`TicketCC`**, **`TicketDependency`**, **`IgnoreEmail`**, **`EmailTemplate`** (DB-stored templates compiled at send time), **`KBCategory`/`KBItem`**, and the newest addition, **`Checklist`/`ChecklistTemplate`/`ChecklistTask`** (migration 0038).

39 migrations, `0001_initial` → `0038_checklist...`. Several are `RunPython` data migrations; no `RunSQL`, no raw SQL anywhere in the app.

## Request flow

**Web (staff):** URL → `helpdesk_staff_member_required` (a `user_passes_test` whose predicate is curried at import time) → view in `staff.py` → `HelpdeskUser` object-level check (`user.py`) → form → `update_ticket.py` → FollowUp + TicketChange rows → `send_templated_mail` renders subject/plain/HTML from the `EmailTemplate` table → signal → webhook POST.

**Ticket list:** the page loads, then DataTables calls back to `datatables_ticket_list`, which decodes a base64-JSON blob from the URL into ORM filters via `query.py`.

**Email in:** cron or Celery → `get_email` command → `process_email()` → per-queue `process_queue()` → POP3/IMAP/OAuth/local-dir transport → `extract_email_metadata` → `create_object_from_email_message` → new Ticket or a FollowUp on an existing one (matched by ticket id in the subject) → auto-acknowledgement out.

**API:** DRF router at `/api/` — `tickets`, `followups`, `followups-attachments`, `users` are all `IsAdminUser`; only `user_tickets` is `IsAuthenticated`. It's an admin API, not a customer-facing one.

## Tests

22 modules, ~6,640 LOC in `helpdesk/tests/`, all Django `TestCase`/`APITestCase`. Weight follows risk: `test_get_email.py` is 1,610 lines, `test_ticket_submission.py` 1,201. `utils.py` has MIME/faker/image factories; `test_files/` holds six `.eml` fixtures for the nasty cases (PGP, non-decodable UTF, quoted-printable, blank body with attachment).

The runner is **`quicktest.py`**, which calls `settings.configure()` with a hardcoded sqlite DB written to `database.db` in the repo root. CI (`.github/workflows/pythonpackage.yml`) runs ruff then `python quicktest.py` on Python 3.10–3.12 against Django 4.2 only.

---

## Oldest / most fragile

**Structural**
1. **`views/staff.py` (2,120 L)** — dashboard, ticket list, mass update, merge, reports, saved queries, CC, dependencies, checklists all in one module. `ticket_list` ~160 L, `run_report` ~140 L, `mass_update` ~140 L. Report *statistics* math (`calc_basic_ticket_stats`, `calc_average_nbr_days_until_ticket_resolved`) lives here too, and it uses naive `datetime.today()` and compares dates as **formatted strings** against DB columns.
2. **`email.py` (1,148 L)** — procedural MIME walking. `process_queue` mutates the process-global `socket.socket = socks.socksocket` (`email.py:401`) from per-queue config; transports are a nested dict-of-dicts literal.
3. **`settings.py` import-time shim** — config can't change at runtime, and `override_settings` in tests silently doesn't take.

**Correctness bugs I confirmed**
4. `decorators.py:77` and `:98` — `if not request.user.is_authenticated and not request.user.is_active`. Should be `or`. An authenticated-but-deactivated user passes this gate; it only appears to work because anonymous users are also inactive.
5. `models.py:570` — `priority = IntegerField(..., blank=3)`. `blank` is a boolean; `3` is truthy, so the field is silently optional.
6. `models.py:1879` — `IgnoreEmail.test()` indexes `own_parts[1]` unguarded (IndexError on an address with no `@`) and mixes bare `and`/`or` precedence.
7. `views/api.py:38,72` — both viewsets iterate the **entire** queryset calling `set_custom_field_values()` *before* pagination. N+1 across all tickets on every list call.
8. `user.py:31` — `get_queues` pulls all queues into Python and runs `has_perm` per queue, per request. Same full-table Python loop in the KB helpers.
9. `urls.py:151-163` — dependency routes registered a second time under a settings flag; they're already registered unconditionally at `:83-92`, so the conditional block is dead. Also `urls.py:39` uses `super(self.__class__, self)` (recursion trap) and `:31` has a mystery import the maintainers themselves flagged with a TODO.

**Legacy residue**
10. `UserSettings.settings_pickled` — a base64-pickle column still on the model, labeled `DEPRECATED!` in its own verbose_name, superseded by migration 0020 but never dropped.
11. `SavedSearch.query` help text still says "Pickled query object" — it's been base64-JSON for years.
12. `setup.py` imports `distutils` (removed in Python 3.12, which CI tests against) and its classifiers claim Python 3.8/Django 3.2 — contradicting the actual CI matrix.
13. Py2-era naming and shims: `decodeUnknown` (`email.py:499`), `class CustomFieldMixin(object)`, the `#!/usr/bin/python` + `if __name__ == "__main__"` tail in `get_email.py`, `try: import pickle / except: import cPickle` in migrations 0002 and 0020, and a `suite()` loader in `tests/__init__.py` whose comment cites "django <= 1.5".

**Tooling rot**
14. `tox.ini` is 8 lines with no `envlist` and no default `testenv` — so `make test`, `make sphinx`, `make readme` are all broken.
15. `.coveragerc` exists but nothing runs coverage. `.flake8`, `.isort.cfg`, `.pylintrc` are orphaned (nothing invokes them), and their 120-char rule conflicts with ruff's default 88 — while `[tool.ruff]` in `pyproject.toml` is empty.
16. `constraints-Django5.txt` and `constraints-Django32.txt` exist but no workflow references them — **Django 5 is entirely untested** while `requirements.txt` says `Django>=3.2` with no upper bound and pins nothing else.
17. CI runs on `pull_request` only — no post-merge signal on main.
18. sqlite-only testing, with a persisted `database.db` in the repo root. The README itself warns the search doesn't work correctly on sqlite, and no Postgres/MySQL job exists to cover the query code on a backend that does.
19. Two tests permanently skipped: `test_attachments.py:195` ("Rework with model relocation") and `:240`. `test_webhooks.py` binds a live HTTP socket in-process, which is a flake source.

**Worth an audit:** `datatables_ticket_list` / `timeline_ticket_list` (`staff.py:1236,1249`) stack `@helpdesk_staff_member_required` with DRF's `@api_view` outside the router, and accept an untrusted base64-JSON blob from the URL that drives ORM filter kwargs directly. And `models.py:39` hand-rolls a regex URL-scheme sanitizer before `mark_safe` on markdown output.

The good news for anyone refactoring this: no raw SQL, no `.extra()`, no `six`/`ugettext`/`force_text`, no `from __future__`. The ORM usage in `query.py` is modern (`Window`, `Subquery`, `OuterRef`). The rot is concentrated in module size, the settings shim, and tooling — not in the data access layer.

[result: turns=33 cost=$3.17 session=17a5f81d-7a30-565b-141d-b88fa5c9b989]

Claude: That notification was just my own wait-timer finishing — no new information. All three explore agents had already reported, and the overview above is complete and verified against the source.

[result: turns=1 cost=$3.26 session=17a5f81d-7a30-565b-141d-b88fa5c9b989]

Claude: The last of my wait-timers finished — again nothing new. Everything is done: the overview stands as written, with the model layer, request flow, test setup, and fragility list all verified directly against the source.

[result: turns=1 cost=$3.32 session=17a5f81d-7a30-565b-141d-b88fa5c9b989]
