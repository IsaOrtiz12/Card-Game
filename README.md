# Card-Game
This is a project is a game made for INST326.
Welcome to Blind Bidding! In this game you and another player will bid secretly bid on mystery cards- each card does something with your money(called "recources" in game)
# How It Works
Everyone starts with 50 in resrouces. In each round they...
  1. Bid a portion of thie resrouces
  2. The higest bidders win the round and reveal a card
  3. The card they bid on amy increase, decrease or have no effect on thier resorces(the card affects recources to the extent that the player bid.
  4. The game ends when there are no cards left or the players run out of resources. 
# Example Card Bid
  card_definitions = {
    "Resource Gain": {"quantity": 5, "effect": "gain", "amount": 10},
    "Resource Loss": {"quantity": 3, "effect": "lose", "amount": 8},
    "Steal Resource": {"quantity": 2, "effect": "steal", "amount": 5},
    "No Effect": {"quantity": 4, "effect": "none", "amount": 0}
}

# What You See
The game will start with Round 1 where both players are shown thier resources(50) and the cards remaining(14), after which each player can bid any ammount of resrouces on the secret card. Their possibliity for gianing, losing, stealing or having no affect is accounted for in the nezt round. 


     
