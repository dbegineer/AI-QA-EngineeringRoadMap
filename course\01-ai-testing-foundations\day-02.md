# Day 2 — Contracts before cleverness

## Objective

Protect what must never be ambiguous before measuring what can vary.

## Theory

Use normal code and normal assertions for JSON shape, required fields, authorised tool arguments, citations, refusals, HTTP status, and latency ceilings. An LLM judge is not an upgrade for a fact a program can check deterministically.

> **Red flag:** Do not ask an LLM whether `citation` is present. Check the field.

## Real-world QA example

An insurance assistant gives a plausible answer but returns no source. The UI cannot show provenance and an auditor cannot trace the claim. That is a contract failure, not a subjective quality debate.

## Build

Read and run `tests/test_contracts.py`. Notice how `pytest.mark.parametrize` makes each product rule visible.

## Break it

Run `pytest --runxfail -k malformed` to see the intentionally broken response violate the response contract. The test is marked expected-failure by default so main stays green.

## Challenge

In `challenges/week-01/contract_challenge.py`, add a deterministic validator that rejects an answer with an unknown citation.

## Interview question

**Which AI checks should never use LLM-as-a-judge?**

Strong answer: schemas, exact permissions, tool arguments, numerical limits, citations/required fields, status codes, and other machine-verifiable rules. Explain that judges are for semantic criteria after validation.

## Go deeper

- [PyTest: getting started](https://docs.pytest.org/en/stable/getting-started.html) — assertions and test discovery from the maintainers.
- [OWASP prompt injection prevention cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) — why input and action controls belong in the design.

## Completion checklist

- [ ] I can define three deterministic contracts for an AI feature.
- [ ] I know why a green semantic score cannot compensate for a missing safety contract.
