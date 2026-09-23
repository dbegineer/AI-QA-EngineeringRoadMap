# Day 3 — Golden datasets and test design

## Objective

Build a small, explainable dataset that represents user risk—not a random prompt collection.

## Theory

A golden dataset is a versioned set of inputs with expectations and tags. Start with high-frequency journeys, high-impact errors, boundaries, known defects, and adversarial attempts. Tags make quality regressions diagnosable: `happy_path`, `boundary`, `unknown_policy`, `security`.

## Real-world QA example

If 80% of support traffic is delivery status but a wrong return-policy answer causes costly exceptions, both deserve cases; risk—not novelty—sets priority.

## Build

Open `labs/01-testing-foundations/data/golden_cases.json`. For every case, identify input, expected decision, required terms, citation, and risk tags.

## Break it

Temporarily remove `opened` from the expected return-policy terms. The suite can still pass, demonstrating why a vague oracle permits a harmful regression. Restore it, then explain the learning.

## Challenge

Add one `boundary` case: an unopened product returned on day 31. State the expected decision and citation. Then add a matching test.

## Interview question

**How do you start an evaluation dataset when no labelled data exists?**

Strong answer: start small with product requirements, support tickets (safely anonymised), domain experts, risk analysis, and observed failures; label criteria clearly; version data; inspect slices rather than chasing a large count.

## Go deeper

- [Your AI Product Needs Evals — Hamel Husain](https://hamelhusain.substack.com/p/evals) — practical argument for evaluation systems and iteration.
- [NIST Generative AI Profile (PDF)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) — governance and measurement context for generative AI risk.

## Completion checklist

- [ ] My cases have explicit expectations and meaningful tags.
- [ ] I can explain why the dataset includes a security case.
