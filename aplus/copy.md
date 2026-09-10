# Amazon A+ content, Claude Code from the Ground Up

Four modules, six images, within Amazon's limit. Text for each module in
page order. Images are in `png/`, named by module and pixel size;
`png/spare/` holds two modules cut for the limit. No URLs anywhere: Amazon rejects A+ text that
points off-site.

## 1. Standard image header with text (`01-header-970x600.png`)

**The whole tool, in the order you will meet it**

Written against Claude Code v2.1.257 and the official documentation as of
1 September 2026, this book takes you from your first session to agents
that keep working after you close the laptop. Permissions and sandboxing,
memory, hooks, MCP servers, plugins, subagents and agent teams, headless
runs in CI, the desktop, web and mobile apps, the Agent SDK, enterprise
rollout, and what all of it costs. Twenty-eight chapters, nine appendices,
and every one of the 169 official documentation pages mapped to the
chapter that covers it.

## 2. Standard four image and text (`02a` to `02d`, 220x220)

**Your first session.** Install, sign in, and learn what a session
actually does: the context window, permission modes and sandboxing,
memory files, and the everyday workflows. Chapters 1 to 7.

**Extend the tool.** Build a real command line project end to end, then
hooks, keybindings and output styles, MCP servers, the browser, and
plugins. Chapters 8 to 13.

**Hand off the work.** Subagents and agent teams, headless runs in GitHub
Actions and GitLab, routines and scheduled tasks, and Claude Code on the
desktop, web and phone. Chapters 14 to 20.

**Teams and enterprise.** Security and best practices, a brownfield
migration of a real Django app, the Agent SDK, analytics, gateways and
cloud providers, and cost control. Chapters 21 to 28.

## 3. Standard single image and sidebar (`03-sidebar-cards-300x400.png`)

**Kept current after print**

Claude Code ships often, so the book comes with a companion site that
lists, newest first, what has changed since this edition and which
chapter it touches. It is updated monthly and the book itself is
re-uploaded each quarter. The five reference appendices are there as
PDFs, generated from the same documentation snapshot as the book.

The two companion projects, a log parsing tool with its plugin and a
Django 4.2 to 5.2 migration, are public repositories with one commit per
plan step, one branch per migration unit, and every session recorded and
published along with the prompt that started it.

Sidebar, **Companion code**:
- Chapter 8: the logsift CLI and its nginx plugin.
- Chapter 23: the django-helpdesk migration, one branch per unit.
- Chapter 24: the Agent SDK triage agent with its run logs.
- Chapter 27: the cost estimator.

## 4. Standard text

**Who it is for**

Working developers who have tried Claude Code and want to stop guessing.
Team leads deciding how to roll it out, what to lock down, and what it
will cost. Engineers who want to build on the Agent SDK. No prior
experience with agentic coding is assumed; comfort with a terminal and
git is.

**About the author**

Waseem Khan is a US Fulbright Scholar with a master's in public policy
and data analytics from Carnegie Mellon University, where he made the
Heinz College Dean's List, and a master's in computer science from NUST.
In nearly two decades as a software and machine learning engineer he has
shipped Android apps with over a million downloads, and as a Deputy
Commissioner in Pakistan's Inland Revenue Service built the fraud
detection and analytics systems that raised audit capacity twenty-fold.
Today he works inside the LLM industry itself, leading a thirty-person
team that creates and audits the training data used to teach frontier AI
models to code and reason, and writing the PhD-level research problems
used to train their deep-research modes. He is also the author of Large
Language Models from the Ground Up.

Claude Code is a product of Anthropic. This book is an independent work
and is not affiliated with or endorsed by Anthropic.
