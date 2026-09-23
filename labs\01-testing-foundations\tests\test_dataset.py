import pytest

from src.evaluators import required_terms_score
from src.support_assistant import answer


def test_every_golden_case_meets_required_terms(golden_cases):
    failures = []
    for case in golden_cases:
        response = answer(case["question"])
        score, missing = required_terms_score(response["answer"], case["required_terms"])
        if score != 1.0 or response["citation"] != case["expected_citation"]:
            failures.append({"id": case["id"], "score": score, "missing": missing, "citation": response["citation"]})
    assert not failures, f"Golden dataset failures: {failures}"


@pytest.mark.parametrize("tag", ["happy_path", "security"])
def test_tagged_slices_are_represented(golden_cases, tag):
    assert any(tag in case["tags"] for case in golden_cases)
