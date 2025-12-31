# research.md

## Unknowns extracted from Technical Context

1. Testing framework: pytest recommended — confirmed.
2. No external dependencies: confirm standard library only is acceptable for CLI.
3. Input parsing approach: choose argparse (standard library) vs custom menu loop.
4. ID generation: thread‑safe auto‑increment integer — approach clarified for single-threaded CLI.

## Decisions

- Decision: Use Python 3.13 standard library only with argparse for command parsing and a minimal interactive menu fallback.
  - Rationale: Meets "No external dependencies" and keeps code simple for a CLI tool. argparse is part of stdlib and suitable for command-based usage; a simple text menu loop will be provided in quickstart for interactive use.
  - Alternatives considered:
    - click (external) — rejected due to external dependency constraint.
    - prompt_toolkit — rejected for same reason.

- Decision: ID generation via an auto‑incrementing integer field managed by the in‑memory store (simple counter).
  - Rationale: Single process, single user; no concurrency concerns in Phase I.
  - Alternatives considered:
    - UUIDs — unnecessary overhead and not in spec.

## Research tasks to complete implementation

- Task: Document CLI commands and example usage for quickstart.md.
- Task: Define data model fields and validation rules for data-model.md.
- Task: Produce OpenAPI contract is NOT applicable for pure CLI; instead produce a simple command contract or CLI reference under /contracts/cli.md.

## Outcome

All NEEDS CLARIFICATION items resolved. Proceed to Phase 1 design artifacts: data-model.md, contracts/cli.md, quickstart.md.
