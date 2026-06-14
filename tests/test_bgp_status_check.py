from logic.bgp_check import validate_bgp_neighbors


def test_bgp_good(bgp_good_data):

    assert validate_bgp_neighbors(
        bgp_good_data
    ) is True


def test_bgp_idle(bgp_idle_data):

    assert validate_bgp_neighbors(
        bgp_idle_data
    ) is False


def test_bgp_low_prefix(bgp_low_prefix_data):

    assert validate_bgp_neighbors(
        bgp_low_prefix_data
    ) is False