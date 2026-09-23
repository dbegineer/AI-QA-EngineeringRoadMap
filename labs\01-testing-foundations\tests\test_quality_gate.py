from src.evaluators import required_terms_score
from src.support_assistant import answer


QUALITY_THRESHOLD = 1.0


def test_quality_gate(golden_cases):
    results = []
    for case in golden_cases:
        response = answer(case["question"])
        score, missing = required_terms_score(response["answer"], case["required_terms"])
        passed = score == 1.0 and response["citation"] == case["expected_citation"]
        results.append({"id": case["id"], "tags": case["tags"], "passed": passed, "missing": missing})

    quality = sum(item["passed"] for item in results) / len(results)
    failed = [item for item in results if not item["passed"]]
    security_failed = [item for item in failed if "security" in item["tags"]]
    assert not security_failed, f"SECURITY QUALITY GATE FAILED: {security_failed}"
    assert quality >= QUALITY_THRESHOLD, f"QUALITY GATE FAILED: score={quality:.0%}; failures={failed}"
