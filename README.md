# Card-Game
This is a project game made for INST326.
Welcome to Blind Bidding! In this game you and another player will bid secretly bid on mystery cards- each card does something with your money(called "resources" in game)

# How It Works
Everyone starts with 50 in resources. In each round they...
  1. Bid a portion of the resources
  2. The card affecting said bid is revealed
  3. The card they bid on can increase, decrease or have no effect on their resources
  4. The game ends when there are no cards left or the players run out of resources.

# What Each Secret Card Does 
The amount a player will lose/gain/steal is determined by the "amount" value for the "Resource Loss" card in card_definitions. 
### Gain: The player who won the bid for this card is set to gain ten resources! 
### Loss: The player who won the bid for this card will lose 8 resources! 
### Steal: The player who won the bid for this card will steal 5 resources!
### No Effect: The winner of this card will have no affect on anyone's resources. 

# What You See
The game will start with Round 1 where both players are shown their resources(50) and the cards remaining(14), after which each player can bid any amount of resources on the secret card. Their possibility for gaining, losing, stealing or having no affect is accounted for in the next round. 

# Start The Game 
In this folder, ensure that you open and run Blind_Bidding.py from your terminal! Do not run Blind.Bidding.py--that one has name errors!

# Interesting Bugs
So our program sometimes will allow players to go into the negative with resources. I mean it's not like our CPU will come find you for credit debt collections but still it's a little awkward when player 2 wins by like 30 because player 1 was in the negative!

# Improvements  
Though it wasn't technically a bug, our program would end the game after one round...and that was sort of meh. We want to aim for something where we can actually play for more than a minute so we (as suggested) added a while loop.
  Now players can play until there are either no cards left or the two are out of resources. 

# What Each of Us Did
     
# Andrew Parson
I created the core game logic that handles each bidding round. I used the max() function to find the highest bid, a list comprehension to collect all players who made that bid (in case of a tie), and an if/else statement inside a for loop to update each player's resources only deducting from the winners. I used dictionary operations as well to store and return the updated player resources, the winning bid, and the list of winners in a structured format. 