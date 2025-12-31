# Quickstart: Phase I — Todo In‑Memory CLI

This quickstart explains how to run and interact with the Phase I in‑memory Todo CLI (Python 3.13+, no external deps).

Prerequisites

- Python 3.13 installed and on PATH
- From the repository root

Run (development)

- If the generated package exposes a module entrypoint, run:

  python -m src

- Or run the CLI script directly (once generated):

  python src/__main__.py

Basic command examples

1) Add a task

- Command (example):
  python -m src add --title "Buy milk" --description "2 liters"

- Expected output:
  Task created: id=1 title='Buy milk' completed=false

Acceptance check:
- After running the add command, run the list command and verify the added task appears with id=1 and completed=false.

2) List tasks

- Command:
  python -m src list

- Expected output (human readable):
  ID  Title       Completed  Description
  1   Buy milk    False      2 liters

3) Update a task (partial update)

- Command:
  python -m src update 1 --title "Buy milk and eggs"

- Expected output:
  Task updated: id=1

Acceptance check:
- Run list and verify title changed, description preserved.

4) Toggle completion

- Command:
  python -m src toggle 1

- Expected output:
  Task 1 completed=true

5) Delete a task

- Command:
  python -m src delete 1

- Expected output:
  Task deleted: id=1

Error examples

- Adding with empty title:
  python -m src add --title ""
  -> Title must not be empty

- Operating on non-existent ID:
  python -m src update 999 --title "x"
  -> Task not found

Testing notes

- The acceptance tests described in the feature spec can be executed manually by following the examples above.
- Unit tests (pytest) should validate model/store behavior (id allocation, validation, state transitions) independent of CLI parsing.

Developer notes

- CLI should support a --json flag to return machine‑parsable outputs for automated tests (optional).
- Keep the CLI parsing to argparse from stdlib to avoid external dependencies.


















