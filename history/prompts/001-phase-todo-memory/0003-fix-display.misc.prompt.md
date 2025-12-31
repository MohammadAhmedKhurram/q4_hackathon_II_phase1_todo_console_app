---
id: 0003
title: Fix display: make PHR visible
stage: misc
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-phase-todo-memory
branch: 001-phase-todo-memory
user: Product Architect (Human)
command: ask: "fix it so that it can be displayed"
labels: [misc,phr,display]
links:
  spec: specs/001-phase-todo-memory/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - history/prompts/001-phase-todo-memory/0001-sp-specify-spec-created.spec.prompt.md
 - history/prompts/001-phase-todo-memory/0001-why-missing-phr-for-sp-specify.misc.prompt.md
 - history/prompts/001-phase-todo-memory/0002-user-cant-see-phr.misc.prompt.md
 - specs/001-phase-todo-memory/spec.md
tests:
 - none
---

## Prompt

fix it so that it can be displayed

## Response snapshot

I verified the PHR files exist under history/prompts/001-phase-todo-memory and are currently untracked by git. To make them reliably visible in git-aware UIs/IDEs they should be added and committed to the repository. Alternatives: I can print file contents here or adjust file placement/permissions.

Files detected (untracked):
- history/prompts/001-phase-todo-memory/0001-sp-specify-spec-created.spec.prompt.md
- history/prompts/001-phase-todo-memory/0001-why-missing-phr-for-sp-specify.misc.prompt.md
- history/prompts/001-phase-todo-memory/0002-user-cant-see-phr.misc.prompt.md

Suggested actions (choose one):
A) Stage & commit these files locally (I will NOT push). Commit message I propose:
   "chore: add backfilled PHRs for 001-phase-todo-memory\n\n🤖 Generated with Claude Code"
B) Print the PHR contents here so you can see them immediately (no repo changes).
C) Do nothing (I'll wait for instructions).

I will proceed only after you confirm which option you want. If you choose A, reply "commit". If B, reply "show". If C, reply "cancel".

## Outcome

- ✅ Impact: PHRs are present on disk under history/prompts/001-phase-todo-memory
- 🧪 Tests: none
- 📁 Files: listed above
- 🔁 Next prompts: your choice (commit/show/cancel)
- 🧠 Reflection: Recommend automating final PHR commit in sp.specify to avoid untracked PHRs

## Evaluation notes

- Failure modes: user IDE not refreshing; files untracked; branch mismatch
- Next experiment: add PHR existence + commit step to sp.specify
