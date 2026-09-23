# Day 5 — From assertions to evaluation

## Objective

Turn a product rubric into a transparent score and release threshold.

## Theory

Exact-string equality is often brittle for language output. First validate hard contracts, then evaluate meaning against an explicit specification: question, context, response, and criteria. This lab uses a transparent required-term evaluator only as a deliberately limited teaching instrument. It can demonstrate a score and a detectable omission, but keyword presence is not proof of correctness, completeness, relevance, or safety and must not be treated as a production semantic evaluator. Later work adds human labels and validated LLM judges.

## Real-world QA example

“Please ship a replacement” and “We will send a replacement” can both satisfy a helpfulness criterion. A proper evaluator checks the decision and required condition rather than forcing identical wording.

## Build

Read `src/evaluators.py` and run `pytest -k quality`. The result contains a score plus missing requirements, making a failed case diagnosable.

## Break it

Remove `unopened` from the assistant's return answer. The quality case fails and identifies the missing term. Restore it.

## Challenge

Implement a `citation_matches` evaluator: it passes only when the response citation equals the case's expected citation.

## Interview question

**When would you use code, humans, and an LLM judge?**

Strong answer: code for objective facts; humans for ground truth and high-stakes/ambiguous judgement; an LLM judge for scalable semantic criteria only after validating it against human-labelled examples. Combine methods rather than treating one score as truth.

## Go deeper

- [Hamel Husain’s evaluation guide](https://hamelhusain.substack.com/p/evals) — a practitioner perspective on iterative evaluation.
- [OpenAI Evals guide](https://platform.openai.com/docs/guides/evals) — official evaluation concepts and workflow.

## Completion checklist

- [ ] I can name one blind spot of a keyword/term evaluator.
- [ ] I can explain the difference between an evaluator score and a release decision.
