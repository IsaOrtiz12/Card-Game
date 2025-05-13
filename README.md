# Card-Game
This is a project is a game made for INST326.
Welcome to Blind Bidding! In this game you and another player will bid secretly bid on mystery cards- each card does something with your money(called "recources" in game)
# How It Works
Everyone starts with 50 in resrouces. In each round they...
  1. Bid a portion of thie resrouces
  2. The card affecting said bid is revealed
  3. The card they bid on amy increase, decrease or have no effect on thier resorces
  4. The game ends when there are no cards left or the players run out of resources.
# What Each Secret Card Does 
### Gain: 
### Loss: 
### Steal:
### No Effect: 

# What You See
The game will start with Round 1 where both players are shown thier resources(50) and the cards remaining(14), after which each player can bid any ammount of resrouces on the secret card. Their possibliity for gianing, losing, stealing or having no affect is accounted for in the nezt round. 

# Start The Game 
In this folder, ensure that you open and run Blind_Bidding.py from your terminal! Do not run Blind.Bidding.py--that one has name errors!

# Interesting Bugs
So our program sometimes will allow players to go into the negative with resources. I mean it's not like our CPU will come find you for credit debt collections but still it's a little awkward when player 2 wins by like 30 becuase player 1 was in the negative!

# Improvemtns 
Though it wasnt technically a bug, our program would end the game after one round...and that was sort of meh. We should aim for something where we can actually play for more than a minute so we (as suggested) added a while loop.
  Now players can play until there are either no cards left or the two are out of resrouces. 
     
