# Assignment Guide

Purpose

This guide helps authors choose an appropriate difficulty, scope and decide when to include starter code or datasets for Mergington High School programming assignments.

Audience

Students in high-school introductory to intermediate programming classes (Python). Adjust scope and scaffolding for skill level.

Difficulty levels

- Beginner — 30–60 minutes. Prereqs: basic syntax, variables, simple I/O. Deliverable: a short script or function. Provide starter code and explicit examples.
- Intermediate — 1–2 hours. Prereqs: loops, conditionals, basic data structures. Deliverable: small program with multiple functions. Provide minimal starter code (scaffold) and 2–3 test cases.
- Advanced — 2+ hours. Prereqs: functions/modules, file I/O, simple libraries. Deliverable: multi-file solution or project. Prefer self-contained instructions and optional starter repo.

Scope & Size

- Keep each assignment focused on 1–2 learning objectives.
- Limit required files to a small set (README, starter-code, optional data). Avoid large datasets.
- Provide clear success criteria and at least 3 example inputs/outputs when applicable.

Starter code guidance

- Include starter code when the task benefits from scaffolding (file I/O setup, argument parsing, test harness).
- Starter code should be minimal (≤100 lines) and documented.
- If using external packages, document installation in the README and prefer standard library when possible.

Testing & Evaluation

- Add a short checklist in the README (expected functions, edge cases, performance constraints).
- Provide a few example test cases; if possible include an automated test script `tests/` or `validate_assignment.py`.

Accessibility & Language

- Use clear, student-friendly language.
- Avoid slang and idioms; keep examples short and well-commented.

Publishing workflow

- Create `assignments/<kebab-id>/README.md` using the template.
- Add starter code and any small datasets.
- Use the skill scripts to register the assignment; do not edit `config.json` manually.

If you want, I can scaffold a new assignment now using these guidelines.