def resource_management_update(player_resources: dict, bid_outcome: dict, 
                        card_effects: dict, min_resource: int = 0, 
                        max_resource = 300) -> dict:
    status_update = {}

    """
    Args:

    player_resources (dict): current resources the players each hold
    bid_outcome (dict): the outcome of the bidding round
    card_effects (dict): the actual card effects on the resources
    min_resource (int): minimum resources
    max_resource (int): maximum resources   



    Returns:
        dict: updated resource amounts 
    """

    for player_num, resource in player_resources.items():
        if player_num == bid_outcome["Winner"]:
            #removes the cost of bidding
            resource -= bid_outcome["bid_cost"]
            #adds the card effect
            resource += card_effects.get("change_resource", 0)


        #checks if player resources are within the range allowed in game
        status = "in_range"
        if resource < min_resource:
            status = "below_range"
        elif resource > max_resource:
            status = "above_range"



        status_update[player_num] = {"resources":resource, "status":status}

    return status_update


