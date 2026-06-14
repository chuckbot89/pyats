import pytest
from logic.bgp_check import validate_bgp_neighbors


# def test_bgp_good(bgp_good_data):

#     assert validate_bgp_neighbors(
#         bgp_good_data
#     ) is True


# def test_bgp_idle(bgp_idle_data):

#     assert validate_bgp_neighbors(
#         bgp_idle_data
#     ) is False


# def test_bgp_low_prefix(bgp_low_prefix_data):

#     assert validate_bgp_neighbors(
#         bgp_low_prefix_data
#     ) is False
    
    
@pytest.mark.parametrize(
    "fixture_name, expected",
    [
        pytest.param("bgp_good_data", True, id="bgp_good"),
        pytest.param("bgp_idle_data", False, id="bgp_idle"),
        pytest.param("bgp_low_prefix_data", False, id="bgp_low_prefix"),
        pytest.param("bgp_no_neighbor_data", False, id="bgp_no_neighbor")
    ]
)
def test_validate_bgp_neighbors(request, fixture_name, expected):

    parsed_output = request.getfixturevalue(fixture_name)

    assert validate_bgp_neighbors(parsed_output) is expected