# Day 7 — Test strategy review and job-ready story

## Objective

Turn the week’s code into a credible test strategy and an interview-ready explanation.

## Your one-page strategy

For the support assistant, write:

1. **Purpose and users:** policy support without invented policy.
2. **Risks:** misinformation, missing provenance, prompt injection, unsafe action, latency.
3. **Contracts:** schema, cited answers, refusal for unknown policy, no secret/system-note disclosure.
4. **Evaluation:** required policy conditions and expected decision by golden case; review false positives/negatives.
5. **Dataset:** versioned cases tagged by risk; additions originate in requirements, incidents, or expert review.
6. **Release gate:** all security contracts pass; quality score meets stated threshold; failure report is reviewed.
7. **Operations later:** log failures safely, turn confirmed production failures into regression cases, periodically relabel.

## Publishable evidence

Complete the [Week 1 checklist](../../challenges/week-01/README.md), run the lab, and add your strategy as a pull request or GitHub discussion. The valuable signal is not “I watched an AI course”; it is “I designed and automated a small AI quality gate, including an injected regression.”

## Challenge

Choose a real product feature you know. Create five golden cases and one safety contract without using customer data. State which cases belong in every pull request versus a scheduled suite.

## Interview questions

1. How do you test a non-deterministic LLM feature?
2. How do you keep a golden dataset from becoming stale?
3. What does a quality gate do when aggregate quality is good but a security slice fails?
4. Why is an LLM judge not automatically reliable?
5. Tell me about a defect you would add to the regression dataset.

Answer signals are in [Week 1 interview prep](../../interview-prep/week-01.md).

## Completion checklist

- [ ] All default lab tests pass.
- [ ] I ran and understood each deliberate failure.
- [ ] I completed the coding challenge without copying a solution first.
- [ ] I can explain contracts, datasets, evaluators, slices, thresholds, and a quality gate.
- [ ] I wrote a one-page test strategy.
