from logic.bgp_check import are_bgp_neighbors_established
import pytest

@pytest.mark.parametrize(
    "parsed_output, expected",
    [
        (
            {
                "neighbor": {
                    "10.1.1.1": {"state": "Established"},
                    "10.1.1.2": {"state": "Established"},
                    "10.1.1.3": {"state": "Idle"}
                    },
            },
                False
            ),
        (
            {
                "neighbor": {
                    "10.1.1.1": {"state": "Established"},
                    "10.1.1.2": {"state": "Established"},
                    "10.1.1.3": {"state": "Established"}
                    },
            },
                True
            ), 
        (
            {
                "neighbor": {
                    "10.1.1.1": {"state": "Established"},
                    "10.1.1.2": {"state": "Established"},
                    "10.1.1.3": {"state": "Active"}
                    },
            },
                False
            ),
        (
            {
                    "neighbor": {}
            },
                False
            ),
    ]
)

def test_are_bgp_neighbors_established(parsed_output, expected):
    assert are_bgp_neighbors_established(parsed_output) == expected