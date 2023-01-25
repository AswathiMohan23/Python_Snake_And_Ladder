from random import randint

from Snake_And_Ladder import game_methods

check = game_methods.optionCheck()
if check == 1:
    value = game_methods.randomCheck()
    print( "------------------------- WOW IT'S A LADDER ------------------------------")
    print("move ahead by ",value)
elif check == 2:
    value = game_methods.randomCheck()
    print("------------------------- OOPS IT'S A SNAKE ------------------------------")
    print( " move behind by ", value)
else:
    print("\nYou dont have chance to play so stay at the same position till your next turn")