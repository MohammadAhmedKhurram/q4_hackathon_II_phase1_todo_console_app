---
id: 0002
title: User can't see PHR
stage: misc
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-phase-todo-memory
branch: 001-phase-todo-memory
user: Product Architect (Human)
command: ask: "but i can't see it"
labels: [misc,phr,visibility]
links:
  spec: specs/001-phase-todo-memory/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-phase-todo-memory/spec.md
 - history/prompts/001-phase-todo-memory/0002-user-cant-see-phr.misc.prompt.md
tests:
 - none
---

## Prompt

but i can't see it

## Response snapshot

Recorded user's visibility issue and confirmed PHRs exist at history/prompts/001-phase-todo-memory/

## Outcome

- ✅ Impact: User message recorded for audit
- 🧪 Tests: none
- 📁 Files: specs/001-phase-todo-memory/spec.md
- 🔁 Next prompts: /sp.plan or manual review
- 🧠 Reflection: Encourage auto-fill of PHR after create-phr.sh

## Evaluation notes (flywheel)

- Failure modes observed: User could not find file due to local IDE refresh or untracked file status
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): 1
- Next experiment (smallest change to try): Add PHR existence check to sp.specify
