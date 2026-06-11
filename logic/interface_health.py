def interface_health_check(parsed_output):
    results = []

    interfaces = parsed_output["interface"]

    for intf_name, intf_data in interfaces.items():
        status = intf_data["status"]
        protocol = intf_data["protocol"]

        if status == "up" and protocol == "up":
            results.append({
                "interface": intf_name,
                "state": "OK",
                "status": status,
                "protocol": protocol
            })

        elif status == "administratively down":
            results.append({
                "interface": intf_name,
                "state": "SKIPPED",
                "status": status,
                "protocol": protocol
            })

        else:
            results.append({
                "interface": intf_name,
                "state": "ALERT",
                "status": status,
                "protocol": protocol
            })

    return results