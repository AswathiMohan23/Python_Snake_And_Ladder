from random import randint


class game_methods:

    current_position = 0
    previous_position = 0
    count = 0

    def __init__(self):
        self.ladder_value = None
        self.snake_value = None

    def randomCheck(self):
        random_number = randint(1, 6)
        return random_number

    def optionCheck(self):
        self.count = self.count +1
        option = randint(0, 2)
        return option

    def ladder(self,ladder_value):
        print("\n WOW IT'S A LADDER ------->>>>>>", end="")
        print("\t\tprevious position : ", self.previous_position)
        print("\t\t\t\t\t\t\t\t\t\tyou got : ", ladder_value)
        self.current_position = self.previous_position + ladder_value
        print("\t\t\t\t\t\t\t\t\t\tmove ahead by ", ladder_value)
        if self.current_position == 100:
            print("\t\t\t\t\t\t\t\t\t\tyour current position : 100 !!!! \n\t\t\t\t\t\t\t\t\t\tYou won")
            print("\n\t\t\t\t\t\tthe dice was thrown ", self.count, " times")
        elif self.current_position > 100:
            print("\t\t\t\t\t\t\t\t\t\tyour current position : ", self.current_position, "\n\t\t\t\t\t\t\t\t\t\tyou reached beyond 100 so go back to your previous position and wait till you get 100")
            self.current_position = self.previous_position
        else:
            print("\t\t\t\t\t\t\t\t\t\tyour current position : ",self.current_position)
            self.previous_position = self.current_position

    def snake(self,snake_value):
        print("\nOOPS IT'S A SNAKE ------>>>>>> ", end="")
        print("\t\tprevious position : ", self.previous_position)
        print("\t\t\t\t\t\t\t\t\tyou got : ", snake_value)
        self.current_position = self.previous_position - snake_value
        if self.current_position > 0:
            print("\t\t\t\t\t\t\t\t\tmove behind by ", snake_value)
            print("\t\t\t\t\t\t\t\t\tyour current position : ", self.current_position)
            self.previous_position = self.current_position
        elif self.current_position <= 0:
            self.previous_position = 0
            print("\t\t\t\t\t\t\t\t\toops!!! go back to zero")
            print("\t\t\t\t\t\t\t\t\tyour current position : ", 0)

    def game(self):
        if self.current_position == 100:
            print("You won the game")

        while self.current_position < 100:
            check = self.optionCheck()
            if check == 1:
                self.ladder_value = self.randomCheck()
                self.ladder(self.ladder_value)
            elif check == 2:
                self.snake_value = self.randomCheck()
                self.snake(self.snake_value)

            else:
                print("\nYou dont have chance to play so stay at the same position till your next turn")


if __name__ =="__main__":

    methods = game_methods()
    methods.game()
