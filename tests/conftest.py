import json
import pytest


@pytest.fixture
def bgp_good_data():
    with open("tests/fixtures/bgp_good.json") as f:
        return json.load(f)


@pytest.fixture
def bgp_idle_data():
    with open("tests/fixtures/bgp_idle.json") as f:
        return json.load(f)


@pytest.fixture
def bgp_low_prefix_data():
    with open("tests/fixtures/bgp_low_prefix.json") as f:
        return json.load(f)