import pytest

from logic.version_check import is_supported_version


@pytest.mark.parametrize(
    "version, expected",
    [
        ("15.2", True),
        ("15.0", True),
        ("12.4", False),
    ]
)
def test_supported_version(version, expected):
    assert is_supported_version(version) == expected