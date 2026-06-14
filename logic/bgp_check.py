def validate_bgp_neighbors(parsed_output):

    neighbors = parsed_output["neighbor"]

    if not neighbors:
        return False

    for neighbor_ip, neighbor_data in neighbors.items():

        state = neighbor_data["state"]
        prefix = neighbor_data["prefixes"]

        if state != "Established":
            return False
        
        elif prefix < 100:
            return False

    return True
    


parsed_output = {
    "neighbor": {
        "10.1.1.1": {
            "state": "Established",
            "prefixes": 100
        },
        "10.1.1.2": {
            "state": "Established",
            "prefixes": 150
        }
    }
}

print(validate_bgp_neighbors(parsed_output))