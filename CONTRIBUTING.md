# Contributing

Thank you for helping make AI quality practice more useful and less noisy.

## Contribution bar

Every lesson or lab contribution must answer: **what production risk does this help a learner detect, prevent, measure, or explain?** Add a small runnable example whenever a concept can be demonstrated in code.

Keep lessons concise and use this sequence: objective, mental model, realistic QA scenario, build, deliberate failure, challenge, interview question, and completion checklist.

## Resource-quality policy

1. Prefer primary/official sources: standards bodies, maintainers, vendors, and original papers.
2. Add expert material only when it contributes a distinct practical perspective. For the initial course, Hamel Husain and Shreya Shankar are the allowed practitioner sources.
3. Verify the exact URL and page title before submitting. Do not use tracking links, link shorteners, copied link lists, or invented URLs.
4. Explain in one sentence why a link is worth a learner's time. One strong link is better than ten loosely related ones.
5. Remove or replace stale, duplicated, paywalled-without-warning, or framework-marketing-only resources.

## Framework neutrality

The course teaches testing and evaluation methods, not product allegiance. A framework may appear only as an optional implementation example. Contributions must state the underlying method, offer a plain-Python or vendor-neutral path where practical, and avoid presenting one tool as the definition of AI quality.

## Avoiding AI-learning sprawl

Do not add a topic because it is trending. New modules require: a defined target role capability, a prerequisite relationship in the roadmap, an executable or inspectable learner outcome, and at least one credible source. Put speculative ideas in a GitHub issue labelled `backlog`.

## Pull requests

- Keep each PR focused on one lesson, lab, resource update, or correction.
- Run `pytest` from `labs/01-testing-foundations` for changes affecting Week 1.
- Preserve the default passing suite. Deliberate failures must be opt-in or marked as expected failures.
- Do not submit secrets, customer data, API keys, or unsafe live attack instructions.
