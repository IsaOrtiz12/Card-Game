def resolve_bid_round(current_card, player_resources, bids):
    """
    Resolves a single round of blind bidding.

    Parameters:
        current_card (str): The identifier of the current card (its effect is unknown for now).
        player_resources (dict): Dictionary of players and their current resources.
                                 Example: {'Andrew': 50, 'CPU1': 60}
        bids (dict): Dictionary of secret bid amounts from each player.
                     Example: {'Andrew': 12, 'CPU1': 20}

    Returns:
        dict: {
            'winning_players': list of player names who won the bid (could be a tie),
            'winning_bid': the amount of the winning bid,
            'updated_resources': updated dict of player resources after bid deduction
        }
    """

    # Determine the highest bid amount
    winning_bid = max(bids.values())

    # Identify all players who submitted the winning bid (could be a tie)
    winning_players = [player for player, bid in bids.items() if bid == winning_bid]

    # Deduct the winning bid only from winners
    updated_resources = {}
    for player, resource in player_resources.items():
        if player in winning_players:
            updated_resources[player] = resource - winning_bid
        else:
            updated_resources[player] = resource  # no change for non-winners

    return {
        'winning_players': winning_players,
        'winning_bid': winning_bid,
        'updated_resources': updated_resources
    }

    
