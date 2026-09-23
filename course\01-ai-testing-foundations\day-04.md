# Day 4 — PyTest as the evaluation harness

## Objective

Use ordinary test-engineering practices—fixtures, parameterisation, and readable failure reports—to run a quality dataset repeatedly.

## Theory

PyTest does not become an AI testing framework merely because it calls a model. It is a reliable harness: arrange a case, act through the application boundary, and assert contracts or evaluator results. Keep provider calls behind an adapter so unit-level quality tests can use fakes.

## Real-world QA example

A team changes both prompt and retrieval settings. Parameterised cases make it clear that the regression occurs only in `unknown_policy`, not everywhere. That is more actionable than “quality dropped.”

## Build

Run `pytest -q` and then `pytest -q -k security`. Inspect `tests/conftest.py` and `tests/test_dataset.py`.

## Break it

In `src/support_assistant.py`, make the injection phrase return the system note. Run `pytest -k injection`; restore the refusal.

## Challenge

Add a fixture that loads the golden cases only once per test session, then add a parametrised test for every `happy_path` case.

## Interview question

**How would you keep LLM tests fast and stable in CI?**

Strong answer: unit-test orchestration with fakes, isolate provider calls, run deterministic contracts on every commit, use a small stable evaluation set for PRs, schedule broader or live-model evaluation separately, record configuration and tolerate legitimate variability only where justified.

## Go deeper

- [PyTest parametrizing tests](https://docs.pytest.org/en/stable/how-to/parametrize.html) — official parameterisation guide.
- [GitHub Actions: get started](https://docs.github.com/en/actions/get-started) — official CI entry point.

## Completion checklist

- [ ] I can locate a failure by test ID and dataset tag.
- [ ] I can explain why live-model tests and deterministic unit tests run at different cadences.
