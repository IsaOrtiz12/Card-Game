import random 

def resolve_bid_round(current_card, player_resources, bids):
    """
    Resolves a single round of blind bidding.

    Parameters:
        current_card (str): The identifier of the current card (its effect is unknown for now).
        player_resources (dict): Dictionary of players and their current resources.
                                 Example: {'Andrew': 50, 'CPU1': 60}
        bids (dict): Dictionary of secret bid amounts from each player.
                     Example: {'Andrew': 12, 'CPU1': 20}2

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

    
def generate_deck(card_definitions):
    """
    Generates the deck of card based on the given card setup.
    
    Each card type has a set number of cards, an effect, and the ammount.
    The function end up building a list where each card is store as a dictionary
    
    Parameters:
        card_definitions: info about each card type, including how many to make,
        what the card does, and how much it affects.
        

    returns: 
        list: a listr of all the cards ready to be used for the game
    """
    
    deck = []
    
    for card_type, properties in card_definitions.items():
        quantity = properties["quantity"]
        effect = properties["effect"]
        amount = properties["amount"]
        
        for _ in range(quantity):
            card = {
                "type": card_type,
                "effect": effect,
                "amount": amount 
            }
            deck.append(card)
        
    return deck


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
        if player_num in bid_outcome["winning_players"]: # Changed to handle multiple winners
            #removes the cost of bidding
            resource -= bid_outcome["winning_bid"]
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

def get_player_bid(player_resources_amount): # Modified to take resource amount
    """
    Prompts the current player to enter their secret bid, validates the input,
    and returns the valid bid amount.

    Args:
        player_resources_amount (int): The current resource total of the player.

    Returns:
        int: A valid bid amount entered by the player.
    """
    while True:
        try:
            bid_str = input(f"Enter your secret bid (0-{player_resources_amount}): ")
            bid = int(bid_str)
            if 0 <= bid <= player_resources_amount:
                return bid
            else:
                print(f"Invalid bid. Please enter a value between 0 and {player_resources_amount}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def display_game_state(player_resources_dict, cards_remaining, last_round_result=None):
    """
    Displays the current state of the game to the players.

    Args:
        player_resources_dict (dict): A dictionary where keys are player names
                                      and values are their current resource totals.
        cards_remaining (int): The number of cards left in the deck.
        last_round_result (dict, optional): Information about the previous round's outcome.
                                           Defaults to None if it's the first round.
                                           Expected keys: 'winner', 'winning_bid', 'revealed_card'.
    """
    print("\n--- Game State ---")
    for player, resources in player_resources_dict.items():
        print(f"{player}: Resources = {resources}")
    print(f"Cards Remaining: {cards_remaining}")

    if last_round_result:
        print("\n--- Last Round Result ---")
        print(f"Winner(s): {', '.join(last_round_result['winning_players'])}") # Handling potential ties
        print(f"Winning Bid: {last_round_result['winning_bid']}")
        print(f"Revealed Card: {last_round_result['revealed_card']}")
    print("--------------------")

def display_round_start(current_round):
    """
    Displays the start of a new bidding round.

    Args:
        current_round (int): The current round number.
    """
    print(f"\n--- Round {current_round} - Bidding Phase ---")

def display_bidding_outcome(bids, winning_players, winning_bid): # Modified to take winning_players
    """
    Displays the bids made by each player and the outcome of the bidding.
    Args:
        bids (dict): A dictionary where keys are player names and values are their bids.
        winning_players (list): The name(s) of the player(s) who won the bid.
        winning_bid (int): The winning bid amount.
    """
    print("\n--- Bidding Outcome ---")
    for player, bid in bids.items():
        print(f"{player} bid: {bid}")
    print(f"Winner(s) of the round: {', '.join(winning_players)} with a bid of {winning_bid}") # Handling potential ties
    print("-----------------------")

def reveal_card(deck):
    """
    Reveals and removes the top card from the deck.

    Args:
        deck (list): The list representing the deck of cards.

    Returns:
        dict or None: The revealed card (dictionary) if the deck is not empty,
                     None otherwise.
    """
    if deck:
        return deck.pop(0)
    else:
        return None

def apply_card_effect(player_resources, revealed_card, winning_players, winning_bid):
    """
    Applies the effect of the revealed card to the winning player(s).

    Args:
        player_resources (dict): Dictionary of player resources.
        revealed_card (dict): The revealed card's information.
        winning_players (list): List of players who won the bid.
        winning_bid (int): The amount of the winning bid.

    Returns:
        dict: Updated player resources.
    """
    updated_resources = player_resources.copy()
    if revealed_card:
        effect = revealed_card["effect"]
        amount = revealed_card["amount"]
        for player in winning_players:
            if effect == "gain":
                updated_resources[player] += amount
                print(f"{player} gained {amount} resources from the card.")
            elif effect == "lose":
                updated_resources[player] -= amount
                print(f"{player} lost {amount} resources from the card.")
            elif effect == "steal":
                # Basic steal logic: Steal from a random other player
                other_players = [p for p in player_resources if p != player and player_resources[p] > 0]
                if other_players:
                    stolen_from = random.choice(other_players)
                    steal_amount = min(amount, player_resources[stolen_from])
                    updated_resources[player] += steal_amount
                    updated_resources[stolen_from] -= steal_amount
                    print(f"{player} stole {steal_amount} resources from {stolen_from}.")
                else:
                    print(f"No one to steal from for {player}.")
            elif effect == "none":
                print(f"The card had no effect on {player}.")
            updated_resources[player] -= winning_bid # Deduct the bid cost for all winners
    return updated_resources

if __name__ == "__main__":
    card_definitions = {
        "Resource Gain": {"quantity": 5, "effect": "gain", "amount": 10},
        "Resource Loss": {"quantity": 3, "effect": "lose", "amount": 8},
        "Steal Resource": {"quantity": 2, "effect": "steal", "amount": 5},
        "No Effect": {"quantity": 4, "effect": "none", "amount": 0}
    }
    
    deck = generate_deck(card_definitions)
    random.shuffle(deck) # Shuffle the deck for randomness

    players = ["Player 1", "Player 2"]
    player_resources = {player: 50 for player in players}
    round_number = 0

    while all(resources > 0 for resources in player_resources.values()) and deck:
        round_number += 1
        display_round_start(round_number)
        display_game_state(player_resources, len(deck), last_round if 'last_round' in locals() else None)

        bids = {}
        for player in players:
            if player_resources[player] > 0: # Only allow players with resources to bid
                bid = get_player_bid(player_resources[player])
                bids[player] = bid
            else:
                print(f"{player} is out of resources and cannot bid.")

        # Remove players with no bids (out of resources)
        active_bids = {player: bid for player, bid in bids.items() if player_resources[player] > 0}

        if not active_bids:
            print("No players have resources to bid. Game over.")
            break

        bid_outcome = resolve_bid_round("current_card", player_resources, active_bids)
        winning_players = bid_outcome['winning_players']
        winning_bid = bid_outcome['winning_bid']
        player_resources = bid_outcome['updated_resources'] # Update resources after bidding

        display_bidding_outcome(active_bids, winning_players, winning_bid)

        revealed_card = reveal_card(deck)
        if revealed_card:
            print(f"\nRevealed Card: {revealed_card['type']}")
            player_resources = apply_card_effect(player_resources, revealed_card, winning_players, winning_bid)
            last_round = {"winning_players": winning_players, "winning_bid": winning_bid, "revealed_card": revealed_card['type']}
        else:
            print("\nNo more cards in the deck.")


    print("\n--- Game Over ---")
    for player, resources in player_resources.items():
        print(f"{player}: Final Resources = {resources}")

    # Determine the winner(s)
    winning_amount = max(player_resources.values())
    winners = [player for player, resources in player_resources.items() if resources == winning_amount]
    if len(winners) == 1:
        print(f"The winner is {winners[0]}!")
    elif winners:
        print(f"It's a tie between {', '.join(winners)}!")
    else:
        print("No one has any resources left!")