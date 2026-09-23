# Day 6 — Regression and quality gates

## Objective

Catch a quality regression before release and describe why it should block deployment.

## Theory

A quality gate compares measured performance with an agreed threshold or baseline. It should report the failed slice, not only a total. Gate only what is stable enough to automate, and pair it with failure review. A threshold is a product-risk decision, not a universal number.

## Real-world QA example

A new prompt makes answers shorter and improves a broad satisfaction score, but causes security refusals to drop from 100% to 0%. A sliced gate blocks the release despite the attractive average.

## Build

Run `pytest -k quality_gate`. The test calculates a score across the golden dataset and applies the release threshold.

## Break it

Set `REGRESSION_MODE=1` before running `pytest -k quality_gate`. The assistant intentionally returns an unsafe response to show a gate failure. Remove the setting afterwards.

PowerShell:

```powershell
$env:REGRESSION_MODE=1; pytest -k quality_gate
Remove-Item Env:REGRESSION_MODE
```

## Challenge

Modify the quality report to show pass rate by tag. Which tag should be a hard block even if the aggregate score passes? Explain your decision.

## Interview question

**What belongs in an AI CI quality gate?**

Strong answer: versioned datasets, stable deterministic contracts, high-risk evaluation slices, latency/cost ceilings where measurable, reproducible model/prompt/configuration metadata, thresholds accepted by product and risk owners, and useful failure artefacts. Avoid one opaque universal score.

## Go deeper

- [GitHub Actions workflows and actions](https://docs.github.com/en/actions/concepts/workflows-and-actions) — official CI concepts.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) — risk management framing behind release decisions.

## Completion checklist

- [ ] I ran the green gate and the deliberately failing gate.
- [ ] I can identify a safety slice that must not be averaged away.
