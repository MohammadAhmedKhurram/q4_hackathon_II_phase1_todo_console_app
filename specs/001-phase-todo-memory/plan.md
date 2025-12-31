# Implementation Plan: Phase I — Todo In‑Memory Console Application

**Branch**: `001-phase-todo-memory` | **Date**: 2025-12-31 | **Spec**: specs/001-phase-todo-memory/spec.md
**Input**: Feature specification from `specs/001-phase-todo-memory/spec.md``

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Create a minimal Python 3.13+ in‑memory todo CLI that implements CRUD for a single Task entity. Use a small modular Python project layout (src/, tests/) with no external dependencies, driven by the spec in specs/001-phase-todo-memory/spec.md.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.13
**Primary Dependencies**: None (standard library only)
**Storage**: In‑memory (process runtime only)
**Testing**: pytest (recommended)
**Target Platform**: Linux/macOS terminal (Python 3.13+)
**Project Type**: Single CLI application
**Performance Goals**: Not applicable (small local tool)
**Constraints**: No external network calls, no filesystem persistence
**Scale/Scope**: Single-user local execution, small codebase (<500 LOC)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Gates:

- Principle: "Spec‑First, Always" — satisfied: we have a spec at specs/001-phase-todo-memory/spec.md.
- Principle: "AI‑Generated Code Only" — NOTE: Implementation must be produced by authorized agent tooling; human edits to generated application code are disallowed by constitution for production artifacts. For this phase (exercise), we will generate code via the agent and place it under a clearly labeled branch. (Violation? no)
- Principle: "Stateless by Default" — The constitution prefers durable backing stores; Phase I is explicitly allowed CRUD‑only in memory as an early prototype in the spec and constitution permits CRUD‑only implementations for early phases. Justification: Phase I spec (Out‑of‑Scope) excludes persistence and is therefore a permitted exception.
- Principle: "Cloud‑Native from Day One" — Not applicable for Phase I (prototype CLI). Documented as a limited-scope exception in Complexity Tracking.
- Principle: "Architecture Guardrails & Traceability" — Implementation must reference Task IDs and Spec sections in generated files and PRs; we will ensure generated artifacts include traceability placeholders.

Check result: PASS with documented exceptions for Phase I prototype.

## Project Structure

### Documentation (this feature)

```text
specs/001-phase-todo-memory/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [REMOVE IF UNUSED] Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# [REMOVE IF UNUSED] Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure: feature modules, UI flows, platform tests]
```

**Structure Decision**: Single project CLI layout. Source tree (root):

```
src/
├── models/        # Task model and related domain logic
├── store/         # In‑memory store implementation
├── cli/           # CLI entrypoint and command parsing
└── __main__.py    # run the CLI

tests/
├── unit/
└── integration/
```

Reference: plan-driven minimal layout; keep modules small and testable.

## Complexity Tracking

No significant constitution violations detected. Phase I exceptions recorded in Constitution Check section.

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
