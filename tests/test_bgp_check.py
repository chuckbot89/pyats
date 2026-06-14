from logic.bgp_check import validate_bgp_neighbors
import pytest


@pytest.mark.parametrize(
    "parsed_output, expected",
    [
        pytest.param(
            {
                "neighbor": {
                    "10.1.1.1": {
                        "state": "Established",
                        "prefixes": 120
                        },
                    "10.1.1.2": {
                        "state": "Established",
                        "prefixes": 150
                        },
                },
            },
            True,
            id="all_established",
        ),
        pytest.param(
            {
                "neighbor": {
                    "10.1.1.1": {
                        "state": "Idle",
                        "prefixes": 120
                        },
                    "10.1.1.2": {
                        "state": "Established",
                        "prefixes": 150
                        },
                },
            },
            False,
            id="idle_neighbor",
        ),
        pytest.param(
            {
                "neighbor": {
                    "10.1.1.1": {
                        "state": "Established",
                        "prefixes": 100
                        },
                },
            },
            True,
            id="boundary_prefix_100",
        ),
        pytest.param(
            {
                "neighbor": {}
            },
            False,
            id="no_neighbors",
        ),
    ]
)
def test_validate_bgp_neighbors(parsed_output, expected):
    assert validate_bgp_neighbors(parsed_output) == expected