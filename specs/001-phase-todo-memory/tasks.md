---

description: "Task list for Phase I — Todo In‑Memory Console App"
---

# Tasks: Phase I — In‑Memory Todo (001-phase-todo-memory)

**Input**: Design documents from `specs/001-phase-todo-memory/` (plan.md, spec.md, data-model.md)

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create minimal project skeleton and entrypoint files so code can be executed and tests added.

- [ ] T001 Create project skeleton and entrypoint files in repo root: create `src/`, `src/models/`, `src/services/`, `src/cli/`, `src/store/`, `src/__main__.py`, and `tests/` (trace: T-001)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement domain model, storage, service, and error types that block all user stories. These must be completed before story-specific work.

- [ ] T002 [P] Create Task domain model in `src/models/task.py` (fields: id:int, title:str, description:str, completed:bool). Include validation that title is non-empty. (trace: T-002)
- [ ] T003 [P] Implement in-memory task repository in `src/store/in_memory_task_store.py` with deterministic auto-increment integer IDs and operations: create, list_all, get_by_id, update, delete. (trace: T-003)
- [ ] T004 Create application TaskService in `src/services/task_service.py` that implements use-cases (add_task, list_tasks, update_task, delete_task, toggle_task). Service must call repository and raise domain/application errors. (trace: T-004)
- [ ] T005 [P] Define domain and application error types in `src/models/errors.py`: `ValidationError`, `TaskNotFoundError`. Use these from service and repository layers. (trace: T-005)
- [ ] T006 Implement CLI scaffolding in `src/cli/commands.py` and `src/cli/ui.py` (menu/command parsing helpers, input validation helpers). CLI must not implement business logic — it should call TaskService. (trace: T-006)

---

## Phase 3: User Stories (Priority order)

Purpose: Implement features by user story so each story is independently testable.

### User Story 1 - Add Task (Priority: P1) 🎯 MVP
Goal: Allow a user to add a new Task with title (required) and optional description.
Independent Test: Run CLI, execute add command with title "Buy milk" and optional description "2 liters", verify task appears with integer id and completed=false.

- [ ] T007 [US1] Implement `add` CLI command handler in `src/cli/commands.py` that prompts for title/description and calls `TaskService.add_task`. (depends on T002,T003,T004)
- [ ] T008 [US1] Add user-visible success/failure messages in `src/cli/ui.py` for add operation (e.g., "Created task #3: Buy milk").

### User Story 2 - View Task List (Priority: P1)
Goal: Show all tasks with ID, Title, Completed status, and optional Description.
Independent Test: Add two tasks then run `list` command and verify both shown.

- [ ] T009 [US2] Implement `list` CLI command in `src/cli/commands.py` that calls `TaskService.list_tasks` and renders tasks via `src/cli/ui.py`. (depends on T003,T004)
- [ ] T010 [US2] Format task listing output in `src/cli/ui.py` to include id, title, completed and description when present.

### User Story 3 - Update / Toggle / Delete (Priority: P2)
Goal: Allow partial updates (title/description), toggle completed, and delete by ID.
Independent Test: Create a task, update its title, toggle completion, delete it, and verify effects.

- [ ] T011 [US3] Implement `update` CLI command in `src/cli/commands.py` that accepts an integer ID and partial fields, calls `TaskService.update_task`. (depends on T002,T003,T004)
- [ ] T012 [US3] Implement `toggle` CLI command in `src/cli/commands.py` that accepts an integer ID and calls `TaskService.toggle_task`. (depends on T003,T004)
- [ ] T013 [US3] Implement `delete` CLI command in `src/cli/commands.py` that accepts an integer ID and calls `TaskService.delete_task`. (depends on T003,T004)

---

## Phase 4: Wire & Run (Integration)

Purpose: Connect all layers and provide a single command to run the application.

- [ ] T014 Wire application entry point in `src/__main__.py` to initialize repository, service, and CLI loop (callable via `python -m src`). Ensure clean startup/shutdown and no global mutable state outside repository. (trace: T-007)

---

## Phase 5: Validate Phase I Acceptance Criteria & Quickstart

Purpose: Manual/automated validation that Phase I meets acceptance criteria in `spec.md`.

- [ ] T015 Create `specs/001-phase-todo-memory/quickstart.md` with step-by-step manual tests for SC-001..SC-004 (add/list/update/delete/toggle and edge cases). Use exact commands to run the app and expected output snippets. (trace: T-008)
- [ ] T016 Run manual validation checklist and record results in `specs/001-phase-todo-memory/validation.md` (manual step: follow quickstart and tick pass/fail for each acceptance check).

---

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T017 [P] Add minimal README entry in `README.md` describing how to run the app (python -m src) and reference the spec and tasks. (optional)
- [ ] T018 [P] Add small unit tests scaffold in `tests/unit/test_task_model.py` and `tests/unit/test_in_memory_store.py` (OPTIONAL - include if tests desired).

---

## Dependencies & Execution Order

- Phase 1 (T001) → Phase 2 (T002..T006) → Phase 3 (T007..T013) → Phase 4 (T014) → Phase 5 (T015..T016)
- Within Phase 2: T002 (model) should exist before service code (T004) uses it; repository (T003) and errors (T005) can be developed in parallel when safe.
- Story tasks depend on Foundational tasks as indicated in task descriptions.

---

## Parallel opportunities

- T002, T003, T005 are marked [P] where they can be implemented in parallel by different contributors (different files, minimal overlap).
- Once Foundational (Phase 2) completes, User Stories 1 (T007..T008) and 2 (T009..T010) can be implemented in parallel by separate contributors.

---

## Counts & Summary

- Total tasks: 18 (T001..T018)
- Tasks per story:
  - US1 (P1): 2 tasks (T007,T008)
  - US2 (P1): 2 tasks (T009,T010)
  - US3 (P2): 3 tasks (T011,T012,T013)
- Foundational tasks (blocking): 5 tasks (T002..T006)
- Suggested MVP scope: Complete T001..T010 (Setup + Foundational + US1 + US2) — minimum to demonstrate add and list (US1+US2).

---

## Acceptance checks (inline)

Each task must include a small acceptance check when completed. Example acceptance checks to use when implementing:

- T002: `src/models/task.py` defines Task dataclass with attributes and raises ValidationError on empty title; unit: instantiate Task with title "x" and with empty title and assert ValidationError.
- T003: repository assigns deterministic integer IDs starting at 1; create two tasks and assert IDs 1 and 2.
- T004: TaskService.add_task returns created Task object or id and does not perform CLI I/O.
- T007: Running `python -m src` and using `add` flow creates a task and outputs: "Created task #1: <title>".

---

## Traceability

All files created must include a short comment referencing the Task ID(s) they implement (e.g., `# Trace: T002`).

---

## Next steps

1. Implement T001 (project skeleton).
2. Implement Foundational tasks T002..T006 (models, repo, service, errors, CLI scaffolding).
3. Implement US1 tasks (T007..T008), run quick manual check from quickstart.md.



