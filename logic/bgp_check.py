def are_bgp_neighbors_established(parsed_output):

    neighbors = parsed_output["neighbor"]

    if not neighbors:
        return False

    for neighbor_ip, neighbor_data in neighbors.items():

        state = neighbor_data["state"]

        if state != "Established":
            return False

    return True
    


parsed_output = {
    "neighbor": {
        "10.1.1.1": {"state": "Established"},
        "10.1.1.2": {"state": "Established"},
        "10.1.1.3": {"state": "Idle"}
    }
}

print(are_bgp_neighbors_established(parsed_output))