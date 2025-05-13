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
    for player_num, resource in player_resources.items():
        if player_num in bid_outcome["winning_players"]:
            resource -= bid_outcome["winning_bid"]
            resource += card_effects.get("change_resource", 0)
        status = "in_range"
        if resource < min_resource:
            status = "below_range"
        elif resource > max_resource:
            status = "above_range"
        status_update[player_num] = {"resources":resource, "status":status}
    return status_update

if __name__ == "__main__":
    card_definitions = { "Resource Gain": {"quantity": 5, "effect": "gain", "amount": 10},
        "Resource Loss": {"quantity": 3, "effect": "lose", "amount": 8},
        "Steal Resource": {"quantity": 2, "effect": "steal", "amount": 5},
        "No Effect": {"quantity": 4, "effect": "none", "amount": 0}
    } 
    
    deck = generate_deck(card_definitions)
    for card in deck: 
        print(card)        
        
        

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


def get_player_bid(player_resources):
    """
    Prompts the current player to enter their secret bid, validates the input,
    and returns the valid bid amount.

    Args:
        player_resources (int): The current resource total of the player.

    Returns:
        int: A valid bid amount entered by the player.
    """
    while True:
        try:
            bid_str = input(f"Enter your secret bid (0-{player_resources}): ")
            bid = int(bid_str)
            if 0 <= bid <= player_resources:
                return bid
            else:
                print(f"Invalid bid. Please enter a value between 0 and {player_resources}.")
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
        print(f"Winner: {last_round_result['winner']}")
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

def display_bidding_outcome(bids, winning_player, winning_bid):
    """
    Displays the bids made by each player and the outcome of the bidding.
    Args:
        bids (dict): A dictionary where keys are player names and values are their bids.
        winning_player (str): The name of the player who won the bid.
        winning_bid (int): The winning bid amount.
    """
    print("\n--- Bidding Outcome ---")
    for player, bid in bids.items():
        print(f"{player} bid: {bid}")
    print(f"Winner of the round: {winning_player} with a bid of {winning_bid}")
    print("-----------------------")

# --- Mock Functions (for demonstration purposes) ---
def mock_reveal_card():
    """
    A mock function that simulates revealing a card.
    In the real game, this would interact with Kevin's card logic.
    """

    effects = ["Resource Gain", "Resource Loss", "No Effect"]
    return random.choice(effects)

def mock_apply_card_effect(player_resources, card_effect, bid_amount, winning_player):
    """
    A mock function that simulates applying the effect of a revealed card.
    In the real game, this would interact with Ibrahim's resource management logic.
    """
    updated_resources = player_resources.copy()
    if card_effect == "Resource Gain":
        gain = random.randint(5, 15)
        updated_resources[winning_player] += gain
        print(f"The card granted {gain} resources to {winning_player}.")
    elif card_effect == "Resource Loss":
        loss = random.randint(5, 10)
        updated_resources[winning_player] -= loss
        print(f"The card cost {loss} resources to {winning_player}.")
    elif card_effect == "No Effect":
        print("The card had no immediate effect.")
    return updated_resources

if __name__ == "__main__":
    # Mock game setup
    players = ["Player 1", "Player 2"]
    player_resources = {"Player 1": 50, "Player 2": 50}
    cards_in_deck = 10
    round_number = 1
    last_round = None

    # Simulate a single round
    display_round_start(round_number)
    display_game_state(player_resources, cards_in_deck, last_round)

    bids = {}
    for player in players:
        bid = get_player_bid(player_resources[player])
        bids[player] = bid

    # Mock bidding winner determination (replace with Andrew's logic)
    winning_player = max(bids, key=bids.get)
    winning_bid = bids[winning_player]

    display_bidding_outcome(bids, winning_player, winning_bid)

    # Mock card reveal and effect application
    revealed_card = mock_reveal_card()
    print(f"\nRevealed Card: {revealed_card}")
    player_resources = mock_apply_card_effect(player_resources, revealed_card, winning_bid, winning_player)
    player_resources[winning_player] -= winning_bid # Deduct the bid cost

    cards_in_deck -= 1
    last_round = {"winner": winning_player, "winning_bid": winning_bid, "revealed_card": revealed_card}

    display_game_state(player_resources, cards_in_deck, last_round) 


