from logic.bgp_check import are_bgp_neighbors_established
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
            False,
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
def test_are_bgp_neighbors_established(parsed_output, expected):
    assert are_bgp_neighbors_established(parsed_output) == expected