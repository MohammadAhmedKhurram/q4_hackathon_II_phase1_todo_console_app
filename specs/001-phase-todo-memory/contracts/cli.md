# CLI Contract

This document describes the CLI commands and their inputs/outputs for the Phase I in-memory Todo application.

Commands:

- add
  - Description: Create a new task
  - Usage: todo add --title "Buy milk" [--description "2 liters"]
  - Inputs:
    - --title (string, required, non-empty)
    - --description (string, optional)
  - Output (success): JSON or human text: "Task created: id=1 title='Buy milk' completed=false"
  - Errors:
    - 400: "Title must not be empty"

- list
  - Description: Show all tasks in memory
  - Usage: todo list
  - Output: Human table or JSON of tasks; each task includes id (int), title (string), completed (bool), description (optional)

- update
  - Description: Update fields of an existing task (partial updates allowed)
  - Usage: todo update <id> [--title "New title"] [--description "...]
  - Inputs:
    - id (integer, required)
    - --title (string, optional)
    - --description (string, optional)
  - Output: "Task updated: id=1"
  - Errors:
    - 404: "Task not found"
    - 400: "Invalid id"

- delete
  - Description: Delete a task by id
  - Usage: todo delete <id>
  - Output: "Task deleted: id=1"
  - Errors:
    - 404: "Task not found"

- toggle
  - Description: Toggle completion status
  - Usage: todo toggle <id>
  - Output: "Task 1 completed=true"
  - Errors:
    - 404: "Task not found"

Notes:
- The CLI supports both human-readable text output and a --json flag for machine consumption (optional).
- IDs are integers and validated on input.
- All state is ephemeral and kept in process memory only.
