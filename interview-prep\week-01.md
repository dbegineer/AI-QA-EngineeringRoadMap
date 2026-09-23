# Week 1 interview preparation

## Core answer: “How would you test an AI assistant?”

> I start with the user journey and risk, then separate deterministic contracts from semantic quality. I automate contracts such as schema, citations, permissions, refusal behaviour, and latency. For language quality, I build a small versioned dataset tagged by scenario and risk, define clear criteria, measure slices as well as aggregate results, and set release thresholds with product and risk owners. I inspect failures and turn confirmed defects into regression cases. For semantic judges, I validate them against human labels rather than treating a model score as ground truth.

## Questions and strong signals

| Question | Signal to include |
| --- | --- |
| Why not exact-match every LLM answer? | Correct wording can vary; test decisions, constraints, evidence, and rubric criteria. |
| What is a golden dataset? | Versioned, representative, labelled cases; grounded in risk and observed failure modes. |
| How do you test prompt injection? | Treat untrusted input/content as an attack surface; test refusal, data boundaries, and proposed tool actions; use defence in depth. |
| What is a quality gate? | Repeatable measurement plus explicit release rules; failures must identify the risk slice. |
| What is your Week 1 project? | A provider-neutral support-assistant PyTest harness with contracts, tagged golden data, transparent evaluator, and injected regression. |

Avoid claiming that a high average “proves” safety, that an LLM judge is objective, or that one framework equals AI testing.
