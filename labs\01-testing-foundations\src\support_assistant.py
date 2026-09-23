"""A deterministic stand-in for an AI support assistant.

The course uses a fake service so tests expose quality engineering mechanics.
Replace this adapter with a real model in a later module, while retaining contracts.
"""
from __future__ import annotations

import os


POLICIES = {
    "return": {"answer": "Unopened devices can be returned within 30 days.", "citation": "RET-30"},
    "shipping": {"answer": "Standard delivery takes 3 to 5 business days.", "citation": "SHP-35"},
}


def answer(question: str) -> dict[str, str]:
    normalized = question.lower()
    if "ignore previous instructions" in normalized:
        if os.getenv("REGRESSION_MODE") == "1":
            return {"answer": "System note: internal policy prompt", "citation": ""}
        return {"answer": "I cannot follow instructions that override policy.", "citation": "SEC-01"}
    if "return" in normalized:
        return POLICIES["return"].copy()
    if "ship" in normalized or "delivery" in normalized:
        return POLICIES["shipping"].copy()
    return {"answer": "I do not have a policy answer for that question.", "citation": "UNKNOWN"}
