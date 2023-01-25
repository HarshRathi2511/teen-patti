# Teen Patti (Indian version of Poker)
Teenpatti is an Indian origin card game. The objective of this game is to make the best 3 card hand as per the hand ranking and to maximize the pot (prize pool) before the showdown for you to win. A standard 52-card pack (without the jokers) is used in this game.

## Rules of the game

### Ranking of the card hands from highest to lowest is

1) Trail (three of a kind) : 3 cards of the same rank. AAA is the best hand in the game.
2) Pure Sequence (Straight Flush): Three consecutive cards of the same suit.
3) Sequence (Straight): Three consecutive cards not all in the same suit.
4) Color (Flush): A flush of 3 cards in the same suit, with the highest card winning in the case of a draw.
5) Pair (two of a kind): A pair of 2 cards of the same rank. In case of a draw, the highest-ranking 3rd card will denote the winner.
6) High Card: When neither the dealer nor player has a pair, then the hand with the highest card wins.

For more detailed rules refer [Deltin](https://www.deltin.com/games/indian-flush-teen-patti#:~:text=In%20this%20game%2C%20the%20dealer,best%20hand%20wins%20the%20round.). 

## Game Play

### Start game
To start the game, run the following command, after successful compilation of the files it will start by asking for player details and once the details are filled all the details will be pushed on the NEAR blockchain. 
```
python3 /path/to/game.py 
```


### Play Actions

There are 3 actions that a TeenPatti registered player can be done using the NEAR CLI, namely:
1) **RAISE** - specify the raise amount,which should not be greater than the number of chips you have(i.e balance amount) in an argument provided to action to raise in the game 

 
2) **FOLD** - when your cards are not good enough ,its better of to fold them using the command line .


 
3) **SHOW** - can only be called when 2 players are left in the game who have not yet folded their cards . After show the winner script runs and the winner is           announced . 

 ### Game Winner
 Whenever the winner of game is found it is declared in the logs when either one of the 2 actions are performed :- 
 1. Only one player is left with unfolded cards and rest of the players jave folded theirs 
 2. When only 2 players remain with unfolded cards and a player calls "show" , then the winner is decided upon the hierarchy of their cards 

All the tokens staked in the game is then transferred to the winner instantly !

## Contributors
Made with 💖 by [Harsh Rathi](https://github.com/harshRathi2511)
