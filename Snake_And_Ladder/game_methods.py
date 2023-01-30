from Snake_And_Ladder.dice_check import dice_check


class game_methods(dice_check):
    def __init__(self):
        self.win = 0
        self.value = 0

    def ladder(self, ladder_value):
        print("\n WOW IT'S A LADDER ------->>>>>>", end="")
        print("\t\tprevious position : ", self.value)
        print("\t\t\t\t\t\t\t\t\t\tyou got : ", ladder_value)
        self.value = self.value + ladder_value
        print("\t\t\t\t\t\t\t\t\t\tmove ahead by ", ladder_value)
        if self.value >= 100:
            print("\t\t\t\t\t\t\t\t\t\tyour current position : You won")
        else:
            print("\t\t\t\t\t\t\t\t\t\tyour current position : ", self.value)

    def snake(self, snake_value):
        print("\nOOPS IT'S A SNAKE ------>>>>>> ", end="")
        print("\t\tprevious position : ", self.value)
        print("\t\t\t\t\t\t\t\t\tyou got : ", snake_value)
        self.value = self.value - snake_value
        if self.value > 0:
            print("\t\t\t\t\t\t\t\t\tmove behind by ", snake_value)
            print("\t\t\t\t\t\t\t\t\tyour current position : ", self.value)
        elif self.value <= 0:
            print("\t\t\t\t\t\t\t\t\toops!!! go back to zero")
            self.value = 0

    def game(self):
        while self.value >= 100:
            print("You won the game")
        while self.value < 100:
            check = self.optionCheck()
            if check == 1:
                ladder_value = self.randomCheck()
                self.ladder(ladder_value)
            elif check == 2:
                snake_value = self.randomCheck()
                self.snake(snake_value)

            else:
                print("\nYou dont have chance to play so stay at the same position till your next turn")

