# AI Quality Engineering

> A GitHub-first, 30-day path from QA Automation Engineer to AI Quality Engineer / AI Test Engineer.

**v0.1 — AI Testing Foundations** is ready to study, run, break, and improve. It is deliberately narrow: seven days that establish the evaluation mindset and a runnable PyTest baseline. It is not a catalogue of AI tools.

## Start here

1. Read the [roadmap](ROADMAP.md) and the [30-day course index](course/README.md).
2. Open the browser-friendly [Week 1 tutorial](docs/week-1.html), or read [Day 1](course/01-ai-testing-foundations/day-01.md).
3. Run the lab:

```bash
cd labs/01-testing-foundations
python -m venv .venv
# Windows: .venv\Scripts\activate   |   macOS/Linux: source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

No API key, model download, or evaluation framework is required. The lab uses a deterministic support assistant so the testing method is visible before model variability is introduced.

## The learning loop

**Learn → Build → Break → Test → Fix → Explain**

An AI Quality Engineer does not merely ask whether a chatbot sounds good. They define risk, build representative datasets, choose suitable measurements, automate regression checks, inspect failures, and set release criteria.

## What you will be able to show after Week 1

- A small but real PyTest suite for an AI-shaped application.
- A golden dataset with normal, boundary, and adversarial cases.
- Deterministic assertions for contracts, citations, safety, and latency.
- A scored quality gate with an intentionally injected regression.
- A concise explanation of where exact assertions end and evaluation begins.

## 30-day map

| Stage | Days | Outcome |
| --- | --- | --- |
| Foundations | 1–7 | Quality model, datasets, PyTest, regression gate |
| LLM testing | 8–10 | Prompt and structured-output testing |
| Evaluation | 11–13 | Rubrics, human labels, judge validation |
| RAG | 14–16 | Retrieval and grounded-answer evaluation |
| Agents + MCP | 17–20 | Tool, trajectory, state, and failure testing |
| Safety + guardrails | 21–23 | Injection, data leakage, policy testing |
| Production quality | 24–26 | Traces, online evaluation, CI quality gates |
| Portfolio + interviews | 27–30 | Capstone, résumé evidence, interview stories |

See the complete [course index](course/README.md). Future weeks are intentionally outlines until they meet the Week 1 runnable-content bar.

## Repository map

```text
ai-quality-engineering/
├── course/                 # 30-day navigation and lessons
├── labs/                   # executable, provider-neutral practice
├── challenges/             # starter tasks and solutions after attempt
├── interview-prep/         # job-focused questions and answer signals
├── resources/              # curated, verified source list
├── capstone/               # eventual AI Quality Lab specification
├── docs/                   # static browser tutorial
└── .github/workflows/      # CI for the runnable lab
```

## Career target

This course prepares evidence for roles such as **AI Quality Engineer**, **AI Test Engineer**, **GenAI QA Engineer**, **AI SDET**, and **LLM Evaluation Engineer**. It builds on the strengths a QA engineer already has: risk-based testing, automation, APIs, regression design, defect analysis, and release judgment.

It does **not** try to turn a learner into a model-training researcher in 30 days.

## Principles

- **Method before framework.** A metric, dataset, risk model, and release rule matter more than a logo on a dashboard.
- **Evidence over vibes.** A passing demo is not a quality claim; a reproducible test and failure analysis are.
- **Small, representative datasets beat giant synthetic dumps.** Start with observed failure modes and grow deliberately.
- **Match the method to the claim.** Use deterministic checks for schemas, status codes, citation identifiers, numeric limits, and tool arguments. Use explicit rubrics and validated semantic evaluation for meaning; never treat keyword presence or an unvalidated LLM judge as ground truth.
- **Safety is a quality attribute.** It belongs in the test plan, not in a final polish phase.
- **No sprawl.** A resource or framework earns entry only if it advances the stated job-ready capability.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request. The resource policy and framework-neutrality rules are there to keep the course durable.

## License and safety

Released under the [MIT License](LICENSE). Please report security concerns privately as described in [SECURITY.md](SECURITY.md); do not open public issues containing secrets, private data, or live exploit details.

