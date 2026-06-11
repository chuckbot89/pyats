from logic.interface_check import count_down_interfaces
import pytest

@pytest.mark.parametrize(
    "parsed_output", "expected",
    [
        (
            {
                "interface": {
                    "GigabitEthernet0/0": {"status": "up "},
                    "GigabitEthernet0/1": {"status": "up "}
                    }
                },
                0
            ),
        (
            {
                "interface": {
                    "GigabitEthernet0/0": {"status": "up"},
                    "GigabitEthernet0/0": {"status": "down"},
                }
            },
            1
        ),
    ]
)
def count_down_interfaces(parsed_output, expected):
    assert count_down_interfaces(parsed_output) == expected
