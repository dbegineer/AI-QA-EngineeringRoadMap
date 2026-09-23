# Roadmap: QA Automation → AI Quality Engineer

## The shift

| Conventional automation | AI quality engineering |
| --- | --- |
| Exact expected output | Criteria, scores, thresholds, and tolerances |
| Stable implementation | Changing model, prompt, retrieval data, tools, and policies |
| Mostly functional defects | Functional, quality, safety, cost, latency, and trust defects |
| Test cases verify behaviour | Datasets and evaluators measure behaviour over time |
| Release when tests pass | Release when defined quality risks are acceptable |

## 30-day sequence

1. **Days 1–7 — AI Testing Foundations:** deterministic versus probabilistic behavior, evaluation specifications, risk, contracts, golden data, PyTest, rubric thinking, regression gates.
2. **Days 8–10 — LLM Testing:** prompt versions, structured outputs, non-determinism, metamorphic checks.
3. **Days 11–13 — Evaluation:** label design, human evaluation, code evaluators, LLM-as-a-judge validation.
4. **Days 14–16 — RAG:** retrieval recall/precision, context relevance, grounding, citations, regressions.
5. **Days 17–20 — Agents and MCP:** tool choice, argument validation, trajectories, state, permissions, timeouts.
6. **Days 21–23 — Security and Guardrails:** prompt injection, sensitive data, tool abuse, red-team datasets.
7. **Days 24–26 — Production Quality:** telemetry, traces, offline/online evaluation, quality gates, incident learning.
8. **Days 27–30 — Portfolio and Career:** AI Quality Lab, project narrative, résumé signals, mock interviews.

## Capability milestones

| Milestone | Evidence, not a certificate |
| --- | --- |
| v0.1: AI Testing Foundations | Week 1 lab passes; injected regression is caught; learner can explain the gate and specify question, context, response, and criteria without relying on keyword matching as semantic truth. |
| v0.2: Evaluation and RAG | A labelled dataset, evaluator report, retrieval diagnosis, and regression comparison. |
| v0.3: Agent Safety | Tool-call contract tests, adversarial cases, and a documented threat model. |
| v1.0: AI Quality Lab | CI quality gate across an LLM/RAG/agent sample with documented release criteria. |

## Career firewall

Before adding a course, tool, or tutorial, ask:

1. Does it help test, evaluate, secure, or operate an AI application?
2. Does it create portfolio evidence for the target roles within 1–3 months?
3. Is it necessary now, rather than a later implementation option?

If the answer is not clearly yes, add it to a backlog issue—not the course.
