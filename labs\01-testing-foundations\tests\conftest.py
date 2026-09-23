import json
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def golden_cases():
    data_path = Path(__file__).parents[1] / "data" / "golden_cases.json"
    return json.loads(data_path.read_text(encoding="utf-8"))
