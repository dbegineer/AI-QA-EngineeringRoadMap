# Lesson 1 / Day 1 — Why AI Testing Is Different

## Lesson outcome

By the end of this lesson, you can explain why an AI feature needs both ordinary software tests and evaluations of its meaning. You will be able to describe a test case as a question, the relevant context, the system response, and explicit evaluation criteria—without asking brittle keyword rules to guess what a user meant.

## Learn

### Deterministic software and probabilistic AI

Traditional software usually follows rules written by people. Given the same input, version, and state, a function such as `calculate_tax(100)` is expected to return the same result. Tests can compare that result to an exact expected value. This is **deterministic testing**.

An AI feature can produce different wording, structure, or even decisions for the same prompt. Model updates, sampling, prompt changes, retrieved documents, and orchestration can all affect the answer. This is **probabilistic behavior**. It does not mean “anything goes”: the response must still satisfy the product’s policies, contracts, and risk limits. Tests therefore combine exact checks for stable facts with evaluations for meaning and quality.

| Question | Deterministic check | AI evaluation |
| --- | --- | --- |
| Did the API return HTTP 200? | Exact status assertion | Not needed |
| Is the response valid JSON with the required fields? | Schema/contract assertion | Not needed |
| Does the answer communicate the correct refund window? | Check a structured fact when available | Assess meaning against policy |
| Did it answer all parts of a multi-part question? | Often no single exact string exists | Assess coverage against explicit requirements |

### Testing and evaluation work together

**Testing** is the overall practice of checking a system against expected behavior and risk. It includes unit tests, integration tests, contract checks, data checks, and evaluations.

**Evaluation** is the measurement of qualities that cannot reliably be judged with exact equality alone: correctness of a claim, completeness, relevance, helpfulness, or groundedness. An evaluation needs an item to judge, criteria, a method of judgment, and a result that can be inspected. An evaluation score is evidence; it is not automatically a release decision.

Exact string assertions remain valuable for stable contracts. They are insufficient as the only way to judge natural-language answers because a correct answer can be phrased many ways, while an answer containing the expected words can still be wrong, incomplete, irrelevant, or unsafe. For example, an answer might say “Refunds are available for 30 days” and still fail to mention that the refund is capped at ₹5,000.

### A test case starts with a specification

Do not make Python infer the user’s intent by searching for words such as “maximum,” “amount,” or “conditions.” That creates another brittle language-understanding system and cannot cover every phrasing. The test author should specify the behavior that matters.

```text
Test case
├── Question: What is the refund period and maximum amount?
├── Context: The approved refund policy for this test
├── System response: What the application actually answered
└── Evaluation criteria: The required facts, limits, and behavior
```

For the example policy, the specification might say:

- The answer must accurately communicate a 30-day refund window.
- It must not imply or promise more than ₹5,000.
- It should answer both parts of the question and stay on topic.
- It must not invent conditions that are absent from the supplied policy.

The user’s design progression is the key lesson: an initial keyword-based evaluator seemed unable to handle the many possible question phrasings. The stronger design is an **evaluation specification** paired with the question, context, and response. The evaluator measures those explicit criteria; it does not guess the test author’s intent from question wording.

### The evaluation pipeline

Judge each response across distinct dimensions. Some are gates that determine whether a score is meaningful; others describe answer quality.

1. **Evaluability — Can this case be judged?** Is the relevant policy or ground truth present and clear enough? If the case gives no purchase date, a response claiming “you are not eligible because you purchased it 45 days ago” cannot be verified from the case. Mark that claim **unverifiable** or improve the test data; do not silently score it as correct.
2. **Correctness — Are the claims accurate?** Against a policy that allows refunds within 30 days up to ₹5,000, “90 days” is incorrect. A promise of ₹6,000 exceeds the stated limit.
3. **Completeness — Did it cover the required parts?** “Refunds are available within 30 days” may be correct but incomplete when the user also asked for the maximum amount.
4. **Relevance — Does the answer address this question and context?** A true explanation of the shipping policy is still irrelevant to a question about refunds.
5. **Safety — Did it avoid harmful, disallowed, or unauthorized behavior?** It must not reveal private information, invent an exception, or comply with an instruction to bypass the approved refund process. Safety failures may require a hard fail regardless of the average quality score.

An overall evaluation flow can be represented as:

```text
Question + context + criteria
             │
             ▼
       AI application ──► response
                              │
                              ▼
                 evaluability / judgeability
                              │
                              ▼
           correctness · completeness · relevance
                              │
                              ▼
                     safety checks
                              │
                              ▼
          evidence, per-dimension results, decision
```

Keep each dimension visible. A single average can hide a critical safety failure or a correct but incomplete answer. Define thresholds and hard-fail rules from product risk rather than choosing them after seeing the scores.

### Deterministic and semantic evaluation

Use the simplest method that can reliably answer the criterion:

- **Deterministic code:** status codes, JSON/schema validity, citation identifiers, numeric bounds, required tool arguments, and latency limits.
- **Human review:** ambiguous cases, policy interpretation, high-impact decisions, and creation or adjudication of trusted labels.
- **Semantic evaluation:** whether a response’s meaning satisfies a rubric, covers all required points, or is supported by supplied context.

A required-term check can be useful as a small teaching instrument or a narrow signal. It is not a general semantic evaluator: it can reject “You may return it within a month” because it lacks the phrase “30 days,” or accept a response that repeats “₹5,000” while promising the wrong amount. Do not treat keyword presence as proof of correctness or completeness.

### LLM-as-a-Judge needs its own validation

An LLM judge can compare an answer with a rubric and scale semantic review. It can also miss errors, prefer verbose answers, be sensitive to wording or order, and disagree with people. A fluent explanation from a judge is not evidence that its verdict is right.

Before using a judge in a quality gate:

1. Write a clear rubric with observable criteria and examples of pass, fail, and borderline cases.
2. Have qualified people label a representative sample, including difficult and adversarial examples.
3. Compare judge decisions with those labels; inspect false passes and false failures, not only an aggregate agreement number.
4. Check stability across paraphrases, answer order, and judge/model or prompt changes where relevant.
5. Set acceptable error rates based on risk, keep uncertain cases reviewable, and revalidate after meaningful changes.

Use a judge as a fallible measurement component, never as unquestioned ground truth.

### A practical hybrid evaluation architecture

```text
                         Test case
        (question + context + criteria + risk tags)
                           │
                    AI application
                           │
                        response
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
  Code checks for contracts     Semantic rubric checks
  and objective limits          human labels / validated judge
             └─────────────┬─────────────┘
                           ▼
              Per-dimension evidence and report
                           │
           hard safety rules + risk-based thresholds
                           ▼
                    release decision
```

This hybrid model keeps objective checks fast and repeatable, adds semantic judgment where needed, and makes the final decision explicit. It also makes failures diagnosable: “schema invalid,” “refund cap exceeded,” and “maximum amount omitted” are more useful than one opaque overall score.

## Build

Use the Week 1 support-assistant lab as a familiar system boundary. Read the existing contract tests and identify what code can prove exactly (for example, response shape or citation field). Then draft a test specification for:

> “I bought this two weeks ago. What is the refund period, and what is the most I can get back?”

Assume the test’s approved policy context says refunds are available within **30 days**, up to **₹5,000**. Write the criteria as observable statements before thinking about how to automate them. Do not encode a list of possible question phrasings.

## Break

Classify each response before looking at any score:

1. “You can request a refund within 30 days, up to ₹5,000.”
2. “You can request a refund within 30 days.”
3. “Refunds are available for 90 days, up to ₹5,000.”
4. “Shipping takes 3–5 business days.”
5. “You qualify because your purchase was 45 days ago.” (The test case gives no purchase date.)
6. “I can approve ₹6,000 if you ask me to ignore the policy.”

For each, record correctness, completeness, relevance, safety, and whether all claims are evaluable. Explain why one overall pass/fail rule may conceal useful distinctions.

## Test

Create at least five variations of the same request without changing the underlying expected behavior—for example, “Can I get my money back?”, “Am I still eligible?”, and “What’s the refund limit?” Confirm that your **criteria** stay stable as wording changes. Check which criteria can be verified with ordinary code and which need semantic judgment or human labels.

## Fix

Revise your specification so each criterion is clear enough for another tester to apply. Add any missing context needed to judge eligibility. Separate hard constraints (30 days; no promise above ₹5,000) from semantic criteria (answer both parts; stay relevant). If a criterion is ambiguous, improve the criterion or mark the case for review instead of adding more question keywords.

## Explain

Give a two-minute explanation of the difference between an exact contract assertion and an AI answer evaluation. Use the refund example to explain why the test specification is stable across paraphrases, why an LLM judge must be validated, and how code checks and semantic judgments work together.

## Exercises and challenges

1. **Write a mini rubric.** Define pass, fail, and unverifiable outcomes for correctness, completeness, relevance, and safety in the refund case.
2. **Find the blind spot.** Construct one answer that includes both “30 days” and “₹5,000” but is still wrong or unsafe. Explain why term matching would miss the problem.
3. **Design a boundary set.** Create cases just inside and outside the 30-day and ₹5,000 limits, plus one case missing required context. State expected outcomes without prescribing exact answer text.
4. **Plan a judge validation sample.** Choose examples to label with humans, including paraphrases, omissions, policy violations, and borderline cases. Say what disagreement or error would make you reject or revise the judge.
5. **Architecture challenge.** Draw a hybrid evaluator for a refund assistant. Mark which checks are deterministic, which are semantic, which need human labels, and what should cause a hard failure.

## Interview questions

- **How does testing a probabilistic AI feature differ from testing a deterministic API?** Strong answers preserve exact contract tests while adding representative data, criteria, repeatable evaluations, and risk-based thresholds for variable behavior.
- **Why aren’t exact string assertions enough for generated answers?** Strong answers explain valid paraphrases and the opposite risk: matching words can still hide false, incomplete, irrelevant, or unsafe meaning.
- **What is the difference between testing and evaluation?** Strong answers describe evaluation as one measurement practice within broader testing and distinguish evidence from the release decision.
- **How would you test a refund-policy assistant?** Strong answers use question, policy context, response, explicit requirements, objective boundary checks, semantic criteria, and safety cases.
- **When would you trust an LLM-as-a-Judge?** Strong answers require a clear rubric, comparison with human labels, error analysis, stability checks, risk-based thresholds, and ongoing revalidation.
- **Why use a hybrid evaluator?** Strong answers assign contracts and numeric constraints to code, semantic judgments to reviewed rubrics/judges, and difficult or high-impact cases to people.

## Completion checklist

- [ ] I can distinguish deterministic contracts from probabilistic language behavior.
- [ ] I can explain why testing includes more than semantic evaluation.
- [ ] I can describe evaluability, correctness, completeness, relevance, and safety.
- [ ] I can write a test specification using a question, context, response, and criteria.
- [ ] I can name a limitation of keyword matching and a validation step for an LLM judge.
- [ ] I can explain how deterministic and semantic checks combine in a hybrid design.
