"""Transparent, intentionally limited evaluators for Week 1."""
from __future__ import annotations


def required_terms_score(answer: str, required_terms: list[str]) -> tuple[float, list[str]]:
    """Return fraction of required terms found and the terms that were missing."""
    normalized = answer.lower()
    missing = [term for term in required_terms if term.lower() not in normalized]
    score = 1.0 if not required_terms else (len(required_terms) - len(missing)) / len(required_terms)
    return score, missing


def response_has_contract(response: dict) -> bool:
    return set(response) == {"answer", "citation"} and all(isinstance(value, str) for value in response.values())
