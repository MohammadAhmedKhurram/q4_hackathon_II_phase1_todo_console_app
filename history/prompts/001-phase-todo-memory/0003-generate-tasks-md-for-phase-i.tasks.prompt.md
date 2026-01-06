---
id: 0003
title: Generate tasks.md for Phase I
stage: tasks
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-phase-todo-memory
branch: 001-phase-todo-memory
user: user@example.com
command: /sp.tasks
labels: ["tasks","automation"]
links:
  spec: specs/001-phase-todo-memory/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-phase-todo-memory/tasks.md
 - specs/001-phase-todo-memory/plan.md
 - specs/001-phase-todo-memory/spec.md
 - specs/001-phase-todo-memory/data-model.md
 - .specify/templates/tasks-template.md
 - .specify/templates/phr-template.prompt.md
 - history/prompts/001-phase-todo-memory/0003-generate-tasks-md-for-phase-i.tasks.prompt.md
 - specs/001-phase-todo-memory/quickstart.md (pending)
 - specs/001-phase-todo-memory/validation.md (pending)
tests:
{{TESTS_YAML}}
---

## Prompt

Phase I — In‑Memory Python Console Todo App
1. Tasking Objective
This document decomposes the Phase I plan into atomic, sequential, AI‑executable tasks.

Each task:

Implements a specific responsibility
Maps directly to the plan and spec
Can be executed independently by AI agents
2. Task Execution Rules
Tasks must be completed in order
Each task produces a reviewable artifact
No task may implement functionality outside Phase I scope
Every file created must reference its Task ID
3. Task List (Ordered)
🔹 T‑001: Initialize Project Skeleton
Objective:
Create the minimal project structure required for Phase I.

Scope:

Create src/ directory
Create subdirectories for:
cli
services
models
storage
utils
Add minimal entry point file
Acceptance Criteria:

Project runs without error
No business logic implemented
Directory structure matches the plan
Traceability:

Plan §9 (Conceptual Project Structure)
🔹 T‑002: Define Domain Task Model
Objective:
Create the Task domain entity.

Scope:

Define Task attributes:
id
title
description
completed
Enforce domain rules (e.g., title required)
Acceptance Criteria:

Task cannot be created with empty title
No persistence or CLI logic present
Traceability:

Spec FR‑1
Plan §5.3 (Domain Layer)
🔹 T‑003: Implement In‑Memory Task Repository
Objective:
Create a repository to store tasks in memory.

Scope:

Store tasks during runtime
Generate unique incremental IDs
Support:
create
retrieve all
retrieve by ID
update
delete
Acceptance Criteria:

Tasks exist only in memory
IDs are unique and deterministic
No business rules implemented
Traceability:

Spec FR‑1 → FR‑4
Plan §5.4 (Storage Layer)
🔹 T‑004: Implement Task Application Service
Objective:
Create the application/service layer that implements use cases.

Scope:

Add task
Update task
Delete task
List tasks
Toggle completion
Validate inputs
Handle errors
Acceptance Criteria:

No CLI logic
No direct storage manipulation outside repository
Clear error handling for invalid operations
Traceability:

Spec FR‑1 → FR‑5
Plan §5.2 (Application Layer)
🔹 T‑005: Define Domain & Application Errors
Objective:
Create explicit error types for predictable failure handling.

Scope:

TaskNotFoundError
ValidationError (e.g., empty title)
Acceptance Criteria:

Errors are raised in service/domain layers
No user‑facing messages here
Traceability:

Plan §8 (Error Handling Strategy)
🔹 T‑006: Implement CLI Interface
Objective:
Create the CLI interaction layer.

Scope:

Display menu or commands
Capture user input
Call application services
Display results and errors
Acceptance Criteria:

No business logic
User receives feedback for every action
Errors are human‑readable
Traceability:

Spec §4 (CLI Interaction Requirements)
Plan §5.1 (CLI Layer)
🔹 T‑007: Wire Application Entry Point
Objective:
Connect all layers into a runnable application.

Scope:

Initialize repository and service
Launch CLI loop
Acceptance Criteria:

Application starts via single command
Clean startup and shutdown
No global mutable state outside repository
Traceability:

Plan §4 (Architecture)
Plan §10 (Design Constraints)
🔹 T‑008: Validate Phase I Acceptance Criteria
Objective:
Ensure Phase I meets all requirements.

Scope:

Manual test of all CRUD operations
Verify in‑memory behavior
Confirm alignment with spec
Acceptance Criteria:

All acceptance criteria in /sp.specify satisfied
No scope creep
Ready for demo
Traceability:

Spec §8 (Acceptance Criteria)
4. Task Dependency Graph

T‑001
  ↓
T‑002 → T‑003
        ↓
       T‑004
        ↓
T‑005 → T‑006
        ↓
       T‑007
        ↓
       T‑008

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/bash/check-prerequisites.sh --json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load design documents**: Read from FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
   - Note: Not all projects have all documents. Generate tasks based on what's available.

3. **Execute task generation workflow**:
   - Load plan.md and extract tech stack, libraries, project structure
   - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
   - If data-model.md exists: Extract entities and map to user stories
   - If contracts/ exists: Map endpoints to user stories
   - If research.md exists: Extract decisions for setup tasks
   - Generate tasks organized by user story (see Task Generation Rules below)
   - Generate dependency graph showing user story completion order
   - Create parallel execution examples per user story
   - Validate task completeness (each user story has all needed tasks, independently testable)

4. **Generate tasks.md**: Use `.specify/templates/tasks-template.md` as structure, fill with:
   - Correct feature name from plan.md
   - Phase 1: Setup tasks (project initialization)
   - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
   - Phase 3+: One phase per user story (in priority order from spec.md)
   - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
   - Final Phase: Polish & cross-cutting concerns
   - All tasks must follow the strict checklist format (see Task Generation Rules below)
   - Clear file paths for each task
   - Dependencies section showing story completion order
   - Parallel execution examples per story
   - Implementation strategy section (MVP first, incremental delivery)

5. **Report**: Output path to generated tasks.md and summary:
   - Total task count
   - Task count per user story
   - Parallel opportunities identified
   - Independent test criteria for each story
   - Suggested MVP scope (typically just User Story 1)
   - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

Context for task generation: Phase I — In‑Memory Python Console Todo App
1. Tasking Objective
This document decomposes the Phase I plan into atomic, sequential, AI‑executable tasks.

Each task:

Implements a specific responsibility
Maps directly to the plan and spec
Can be executed independently by AI agents
2. Task Execution Rules
Tasks must be completed in order
Each task produces a reviewable artifact
No task may implement functionality outside Phase I scope
Every file created must reference its Task ID
3. Task List (Ordered)
🔹 T‑001: Initialize Project Skeleton
Objective:
Create the minimal project structure required for Phase I.

Scope:

Create src/ directory
Create subdirectories for:
cli
services
models
storage
utils
Add minimal entry point file
Acceptance Criteria:

Project runs without error
No business logic implemented
Directory structure matches the plan
Traceability:

Plan §9 (Conceptual Project Structure)
🔹 T‑002: Define Domain Task Model
Objective:
Create the Task domain entity.

Scope:

Define Task attributes:
id
title
description
completed
Enforce domain rules (e.g., title required)
Acceptance Criteria:

Task cannot be created with empty title
No persistence or CLI logic present
Traceability:

Spec FR‑1
Plan §5.3 (Domain Layer)
🔹 T‑003: Implement In‑Memory Task Repository
Objective:
Create a repository to store tasks in memory.

Scope:

Store tasks during runtime
Generate unique incremental IDs
Support:
create
retrieve all
retrieve by ID
update
delete
Acceptance Criteria:

Tasks exist only in memory
IDs are unique and deterministic
No business rules implemented
Traceability:

Spec FR‑1 → FR‑4
Plan §5.4 (Storage Layer)
🔹 T‑004: Implement Task Application Service
Objective:
Create the application/service layer that implements use cases.

Scope:

Add task
Update task
Delete task
List tasks
Toggle completion
Validate inputs
Handle errors
Acceptance Criteria:

No CLI logic
No direct storage manipulation outside repository
Clear error handling for invalid operations
Traceability:

Spec FR‑1 → FR‑5
Plan §5.2 (Application Layer)
🔹 T‑005: Define Domain & Application Errors
Objective:
Create explicit error types for predictable failure handling.

Scope:

TaskNotFoundError
ValidationError (e.g., empty title)
Acceptance Criteria:

Errors are raised in service/domain layers
No user‑facing messages here
Traceability:

Plan §8 (Error Handling Strategy)
🔹 T‑006: Implement CLI Interface
Objective:
Create the CLI interaction layer.

Scope:

Display menu or commands
Capture user input
Call application services
Display results and errors
Acceptance Criteria:

No business logic
User receives feedback for every action
Errors are human‑readable
Traceability:

Spec §4 (CLI Interaction Requirements)
🔹 T‑007: Wire Application Entry Point
Objective:
Connect all layers into a runnable application.

Scope:

Initialize repository and service
Launch CLI loop
Acceptance Criteria:

Application starts via single command
Clean startup and shutdown
No global mutable state outside repository
Traceability:

Plan §4 (Architecture)
Plan §10 (Design Constraints)
🔹 T‑008: Validate Phase I Acceptance Criteria
Objective:
Ensure Phase I meets all requirements.

Scope:

Manual test of all CRUD operations
Verify in‑memory behavior
Confirm alignment with spec
Acceptance Criteria:

All acceptance criteria in /sp.specify satisfied
No scope creep
Ready for demo

## Task Generation Rules

**CRITICAL**: Tasks MUST be organized by user story to enable independent implementation and testing.

**Tests are OPTIONAL**: Only generate test tasks if explicitly requested in the feature specification or if user requests TDD approach.

### Checklist Format (REQUIRED)

Every task MUST strictly follow this format:

```text
- [ ] [TaskID] [P?] [Story?] Description with file path
```

**Format Components**:

1. **Checkbox**: ALWAYS start with `- [ ]` (markdown checkbox)
2. **Task ID**: Sequential number (T001, T002, T003...) in execution order
3. **[P] marker**: Include ONLY if task is parallelizable (different files, no dependencies on incomplete tasks)
4. **[Story] label**: REQUIRED for user story phase tasks only
   - Format: [US1], [US2], [US3], etc. (maps to user stories from spec.md)
   - Setup phase: NO story label
   - Foundational phase: NO story label
   - User Story phases: MUST have story label
   - Polish phase: NO story label
5. **Description**: Clear action with exact file path

**Examples**:

- ✅ CORRECT: `- [ ] T001 Create project structure per implementation plan`
- ✅ CORRECT: `- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py`
- ✅ CORRECT: `- [ ] T012 [P] [US1] Create User model in src/models/user.py`
- ✅ CORRECT: `- [ ] T014 [US1] Implement UserService in src/services/user_service.py`
- ❌ WRONG: `- [ ] Create User model` (missing ID and Story label)
- ❌ WRONG: `T001 [US1] Create model` (missing checkbox)
- ❌ WRONG: `- [ ] [US1] Create User model` (missing Task ID)
- ❌ WRONG: `- [ ] T001 [US1] Create model` (missing file path)

... (truncated for brevity)

## Response snapshot

Generated `specs/001-phase-todo-memory/tasks.md` containing 18 tasks organized by phase and user story. Created PHR at `history/prompts/001-phase-todo-memory/0003-generate-tasks-md-for-phase-i.tasks.prompt.md`. Summary: Total tasks 18; Foundational tasks 5; US1 tasks 2; US2 tasks 2; US3 tasks 3; MVP suggestion: T001..T010.

## Outcome

- ✅ Impact: Created tasks.md and staged PHR for Phase I tasks generation.
- 🧪 Tests: None run (manual generation of tasks.md).
- 📁 Files: specs/001-phase-todo-memory/tasks.md (created), history/prompts/001-phase-todo-memory/0003-generate-tasks-md-for-phase-i.tasks.prompt.md (this file)
- 🔁 Next prompts: Implement T001 (project skeleton) and foundational tasks T002..T006.
- 🧠 Reflection: Tasks generated following /sp.tasks outline; ready for implementation. No unresolved placeholders remain.

## Evaluation notes (flywheel)

- Failure modes observed: None observed during generation.
- Graders run and results (PASS/FAIL): N/A - no graders run.
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A - manual follow-up to implement T001.
