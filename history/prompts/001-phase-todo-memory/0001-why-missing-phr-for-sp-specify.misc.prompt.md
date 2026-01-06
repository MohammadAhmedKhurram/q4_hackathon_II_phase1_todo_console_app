---
id: 0001
title: Why missing PHR for sp.specify
stage: misc
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-phase-todo-memory
branch: 001-phase-todo-memory
user: Product Architect (Human)
command: ask: "Why didn't you record the phr of /sp.specify of 001-phase-todo-memory?"
labels: [misc, phr, sp.specify]
links:
  spec: specs/001-phase-todo-memory/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - history/prompts/001-phase-todo-memory/0001-why-missing-phr-for-sp-specify.misc.prompt.md
 - specs/001-phase-todo-memory/spec.md
tests:
 - none
---

## Prompt

Why didn't you record the phr of /sp.specify of 001-phase-todo-memory ?

## Response snapshot

Short answer

- The /sp.specify run produced the spec (specs/001-phase-todo-memory/spec.md) but did not produce a completed PHR because PHR creation is an explicit, agent-driven step: the helper script (.specify/scripts/bash/create-phr.sh) only copies the template and leaves {{PLACEHOLDERS}} for the AI agent to fill — the agent must fill and save the file. See the script header that documents this behavior at .specify/scripts/bash/create-phr.sh:21-26.

Evidence & references

- create-phr behavior: .specify/scripts/bash/create-phr.sh:21-26 ("The calling AI agent is responsible for filling {{PLACEHOLDERS}}")
- sp.specify requirement: .claude/commands/sp.specify.md:261-283 (instructs the agent to create and complete a PHR as the main request completes)
- Spec file exists: specs/001-phase-todo-memory/spec.md:2 (Feature Branch: `001-phase-todo-memory`)
- Prompts dir contents (no completed spec-stage PHR found): history/prompts/001-phase-todo-memory/ — currently contains only this misc PHR file.

Likely root causes (ordered):
1. The agent ran the spec generation but skipped the final PHR-fill step (most likely). Many flows run the create-phr.sh fallback but forget to replace placeholders.
2. The create-phr.sh script was not executed by whatever ran sp.specify (create-new-feature.sh creates the prompts dir but does not itself fill a PHR).
3. Environment/permission/branch-detection issues prevented creation (unlikely here given specs and prompts dir exist).

Remediation taken

- I have recorded your question verbatim in this PHR at: history/prompts/001-phase-todo-memory/0001-why-missing-phr-for-sp-specify.misc.prompt.md

Options

- I can backfill the missing spec-stage PHR now by generating a spec-stage PHR from specs/001-phase-todo-memory/spec.md and saving it to history/prompts/001-phase-todo-memory/ (I will ask before writing). Would you like me to backfill it? (yes/no)

Outcome

- ✅ Impact: Current user question recorded as a PHR under the feature.
- 🧪 Tests: none
- 📁 Files: specs/001-phase-todo-memory/spec.md; history/prompts/001-phase-todo-memory/0001-why-missing-phr-for-sp-specify.misc.prompt.md
- 🔁 Next prompts: Backfill the /sp.specify spec-stage PHR? (Y/N)
- 🧠 Reflection: Recommend making PHR creation a mandatory, automated final step in sp.specify flows to avoid manual omission.

## Evaluation notes

- Failure modes observed: missing/unfinished PHRs when agents use script fallback without filling placeholders.
- Graders run and results (PASS/FAIL): N/A
- Next experiment: Add an automated check that verifies a completed PHR exists after /sp.specify and fails the workflow if it does not.
