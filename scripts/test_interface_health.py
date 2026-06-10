from interface_health import interface_health_check


def test_interface_health_check():
    sample_output = {
        "interface": {
            "GigabitEthernet0/0": {
                "status": "up",
                "protocol": "up"
            },
            "GigabitEthernet0/1": {
                "status": "administratively down",
                "protocol": "down"
            },
            "GigabitEthernet0/2": {
                "status": "down",
                "protocol": "down"
            }
        }
    }

    results = interface_health_check(sample_output)

    assert results[0]["state"] == "OK"
    assert results[1]["state"] == "SKIPPED"
    assert results[2]["state"] == "ALERT"