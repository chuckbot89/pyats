import json
import pytest
from logic.bgp_check import validate_bgp_neighbors


@pytest.fixture
def bgp_low_prefix_data():

    with open("tests/fixtures/bgp_low_prefix.json") as f:
        return json.load(f)


def test_bgp_low_prefix(bgp_low_prefix_data):

    assert validate_bgp_neighbors(bgp_low_prefix_data) is False