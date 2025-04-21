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

if __name__ == "__main__":
    card_definitions = { "Resource Gain": {"quantity": 5, "effect": "gain", "amount": 10},
        "Resource Loss": {"quantity": 3, "effect": "lose", "amount": 8},
        "Steal Resource": {"quantity": 2, "effect": "steal", "amount": 5},
        "No Effect": {"quantity": 4, "effect": "none", "amount": 0}
    } 
    
    deck = generate_deck(card_definitions)
    for card in deck: 
        print(card)        