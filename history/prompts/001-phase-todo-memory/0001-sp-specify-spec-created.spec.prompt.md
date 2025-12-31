---
id: 0001
title: sp.specify: spec created (backfill)
stage: spec
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-phase-todo-memory
branch: 001-phase-todo-memory
user: Product Architect (Human)
command: sp.specify -- "Phase I — Todo In‑Memory Console Application"
labels: [spec,phr,backfill]
links:
  spec: specs/001-phase-todo-memory/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-phase-todo-memory/spec.md
 - history/prompts/001-phase-todo-memory/0001-sp-specify-spec-created.spec.prompt.md
tests:
 - none
---

## Prompt

# Feature Specification: Phase I — Todo In‑Memory Console Application

**Feature Branch**: `001-phase-todo-memory`
**Created**: 2025-12-31
**Status**: Draft
**Input**: User description: "Phase I — Todo In‑Memory Console Application
1. Phase Objective
The objective of Phase I is to create a minimal, deterministic, in‑memory Todo application that establishes:

Core domain model (Task)
CRUD workflows
Clean separation of concerns
Spec‑driven development discipline
This phase serves as the foundation for all future phases.

2. User Persona
Primary User:
A single local user interacting via a terminal.

No authentication
No persistence beyond runtime
One Todo list per execution
3. Functional Requirements (WHAT)
FR‑1: Add Task
Description:
The user can create a new todo task.

Input:

Title (required)
Description (optional)
Rules:

Title must not be empty
Task is assigned a unique ID
Task defaults to completed = false
FR‑2: View Task List
Description:
The user can view all tasks currently in memory.

Displayed Fields:

ID
Title
Completion status
Optional description
FR‑3: Update Task
Description:
The user can update an existing task.

Editable Fields:

Title
Description
Rules:

Task ID must exist
Partial updates are allowed
FR‑4: Delete Task
Description:
The user can delete a task by ID.

Rules:

Task ID must exist
Deleted tasks are permanently removed from memory
FR‑5: Mark Task Complete / Incomplete
Description:
The user can toggle a task’s completion status.

Rules:

Task ID must exist
Toggle switches true ↔ false
4. CLI Interaction Requirements
Application runs from terminal
Menu‑based or command‑based interaction is acceptable
User receives clear feedback after every action
Errors are human‑readable (e.g., “Task not found”)
5. Data Model (Conceptual Only)
Task
Field    Type    Notes
id    integer    Auto‑incremented
title    string    Required
description    string    Optional
completed    boolean    Default false
⚠️ This is a conceptual model, not an implementation spec.

6. Non‑Functional Requirements
Runs on Python 3.13+
No external dependencies required
Code must be modular (not a single giant script)
Designed to be easily extended in later phases
7. Explicit Out‑of‑Scope (Phase I)
Databases
Filesystem persistence
Web interfaces
Authentication
AI features
Kubernetes or Docker
8. Acceptance Criteria ✅
Phase I is considered complete when:

✅ User can add, view, update, delete tasks
✅ Tasks exist only in memory
✅ Application runs cleanly from terminal
✅ All behavior maps back to this spec
✅ No code exists without a Task ID (later enforced)"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Task (Priority: P1)

A local user starts the application and creates a new todo task by entering a title and optional description.

Why this priority: Core value — without the ability to add tasks the app provides no value.

Independent Test: Run the application, use the "add" command or menu option to add a task with title "Buy milk" and optional description "2 liters"; verify the task appears in the list with an auto-incremented integer ID and completed=false.

Acceptance Scenarios:

1. Given the app is running and no tasks exist, When the user creates a task with title "X", Then the task is added with a unique integer ID, stored in memory, and completed=false.
2. Given a non-empty title, When the user omits description, Then the task is added and description is empty or omitted without error.

---

### User Story 2 - View Task List (Priority: P1)

A local user requests to view all tasks; the app displays ID, Title, Completion status, and optional description.

Why this priority: Visibility is required to confirm task creation and state.

Independent Test: Add two tasks and run the "list" command; verify both tasks are shown with correct fields.

Acceptance Scenarios:

1. Given tasks exist in memory, When the user requests the list, Then the UI shows all tasks with ID, Title, Completed status, and Description (if present).

---

### User Story 3 - Update / Toggle / Delete (Priority: P2)

A local user updates a task's title or description, toggles completion status, or deletes a task by ID.

Why this priority: Management of existing tasks is necessary for basic todo workflows.

Independent Test: Create a task, then update its title; verify the change. Toggle its completion status; verify it flips. Delete it by ID and verify it no longer appears in the list.

Acceptance Scenarios:

1. Given a task with ID N exists, When the user updates title/description (partial updates allowed), Then the task reflects the changes in memory.
2. Given a task with ID N exists, When the user toggles completion, Then completed switches true ↔ false.
3. Given a task with ID N exists, When the user deletes the task, Then the task is removed from memory and subsequent list does not show it.

---

### Edge Cases

- Adding a task with an empty title should be rejected with a human-readable error.
- Updating, toggling, or deleting a non-existent ID should return "Task not found".
- IDs are integers and must be validated on user input.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow a user to create a task with a non-empty title and optional description. On success return the assigned integer ID and status completed=false.
- **FR-002**: System MUST present a list of all tasks in memory showing ID, Title, Completed status, and Description when requested.
- **FR-003**: System MUST allow partial updates to a task (title and/or description) given a valid task ID.
- **FR-004**: System MUST allow deletion of a task by valid task ID; deletion permanently removes the task from memory.
- **FR-005**: System MUST allow toggling a task's completed boolean given a valid task ID.

### Key Entities

- **Task**: Represents a todo item with attributes:
  - id (integer, auto-incremented)
  - title (string, required)
  - description (string, optional)
  - completed (boolean, default false)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A user can add a task with title and optional description and immediately see it in the task list (observable by manual test).
- **SC-002**: Basic CRUD operations succeed in the running process: add, view, update, delete, toggle — each returns human-readable confirmation messages.
- **SC-003**: Errors for invalid operations (empty title, missing ID) are human-readable and reference the cause (e.g., "Task not found", "Title must not be empty").
- **SC-004**: The application runs with no external dependencies on Python 3.13+ and exits cleanly without unhandled exceptions for normal flows.

## Assumptions

- Single local user, single in-memory task list per execution.
- No authentication or persistence beyond runtime.
- CLI-based interaction; exact commands/menu names can be finalized during implementation.

## Acceptance Criteria Mapping

- FR-001 → SC-001, SC-002
- FR-002 → SC-001, SC-002
- FR-003 → SC-002, SC-003
- FR-004 → SC-002, SC-002
- FR-005 → SC-002

## Files and Paths

- Spec file: specs/001-phase-todo-memory/spec.md
- Checklist: specs/001-phase-todo-memory/checklists/requirements.md

## Response snapshot

Backfilled PHR: spec file exists at specs/001-phase-todo-memory/spec.md and summarised here.

## Outcome

- ✅ Impact: Spec backfilled into history/prompts for audit
- 🧪 Tests: none
- 📁 Files: specs/001-phase-todo-memory/spec.md
- 🔁 Next prompts: /sp.plan or manual review
- 🧠 Reflection: Automate PHR completion in sp.specify

## Evaluation notes (flywheel)

- Failure modes observed: Missing placeholder fill after create-phr.sh
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): 1
- Next experiment (smallest change to try): Add PHR existence check to sp.specify script
