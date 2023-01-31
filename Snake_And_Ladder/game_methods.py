from random import randint

player1 = "PLAYER1"
player2 = "PLAYER2"


class game_methods:
    current_position = 0
    previous_position = 0
    count = 0
    flag = 0
    ladder_dict = {1: 38, 4: 14, 9: 31, 28: 84, 21: 42, 51: 67, 80: 99, 72: 91}
    snake_dict = {17: 7, 62: 19, 64: 60, 87: 36, 54: 34, 93: 73, 95: 75, 98: 79}
    player = ""
    other_player = ""

    def __init__(self):
        self.ladder_value = None
        self.snake_value = None
        self.random_value = None

    def randomCheck(self):
        random_number = randint(1, 6)
        return random_number

    def optionCheck(self):
        self.count = self.count + 1
        option = randint(0, 2)
        return option

    def player_check(self):
        random_number = randint(1, 2)
        return random_number

    def ladder(self):
        print("\n WOW  IT'S A LADDER FOR ", self.player, " ------->>>>>>", end="")
        print("\t\tprevious position : ", self.previous_position)
        print("\t\t\t\t\t\t\t\t\t\t\t\t\tladder goes to : ", self.ladder_value)
        print("\t\t\t\t\t\t\t\t\t\t\t\t\tmove ahead by ", self.ladder_value)
        self.current_position = self.ladder_value
        if self.current_position == 100:
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tyour current position : 100 !!!!\n\t\t\t\t\t\t\t\tthe dice was thrown ",
                  self.count, " times")
        elif self.current_position > 100:
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tyour current position : ", self.current_position,
                  "\n\t\t\t\t\t\t\t\t\t\t\t\t\tyou reached beyond 100 so go back to your previous position and wait till you get 100")
            self.current_position = self.previous_position
        else:
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tyour current position : ", self.current_position)
            self.previous_position = self.current_position

        temp = self.player
        self.player = self.other_player
        self.other_player = temp

    def snake(self):
        print("\nOOPS IT'S A SNAKE FOR ", self.player, " ------>>>>>> ", end="")
        print("\t\tprevious position : ", self.previous_position)
        print("\t\t\t\t\t\t\t\t\t\t\t\t\tyou got : ", self.snake_value)
        self.current_position = self.snake_value
        if self.current_position > 0:
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tmove behind by ", self.snake_value)
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tyour current position : ", self.current_position)
            self.previous_position = self.current_position
        elif self.current_position <= 0:
            self.current_position = 0
            self.previous_position = 0
            print("\t\t\t\t\t\t\t\t\t\t\t\t\toops!!! go back to zero")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tyour current position : ", 0)
        temp = self.player
        self.player = self.other_player
        self.other_player = temp

    def normal(self):
        self.count = self.count + 1
        print("\t\t\t\t\t\t\t\tprevious position : ", self.previous_position)
        print("\t\t\t\t\t\t\t\t\t\t\t\t\tyou got : ", self.random_value)
        print("\t\t\t\t\t\t\t\t\t\t\t\t\tmove ahead by ", self.random_value)
        self.current_position = self.previous_position + self.random_value
        if self.current_position in self.ladder_dict.keys():
            self.ladder_value = self.ladder_dict.get(self.current_position)
            self.ladder()
        elif self.current_position in self.snake_dict.keys():
            self.snake_value = self.snake_dict.get(self.current_position)
            self.snake()
        if self.current_position == 100:
            print(
                "\t\t\t\t\t\t\t\t\t\t\t\t\tyour current position : 100 !!!!\n\t\t\t\t\t\t\t\t\t\t\t\t\tthe dice was thrown ",
                self.count, " times")
            print("\n***************------------------- You won the game ---------------------****************")
        elif self.current_position > 100:
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tyour current position : ", self.current_position,
                  "\nyou reached beyond 100 so go back to your previous position and wait till you get 100")
            self.current_position = self.previous_position
        else:
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tyour current position : ", self.current_position)
            self.previous_position = self.current_position

        temp = self.player
        self.player = self.other_player
        self.other_player = temp

    def game(self, player, other_player):
        try:
            while self.current_position < 100:
                print("\nits your turn ", player, end="")
                self.random_value = self.randomCheck()
                self.normal()
        except Exception:
            print("\n current : ", self.current_position, "\n ladder : ",
                  self.ladder_value, "\n snake : \n prev : ", self.previous_position, "\ncount = ", self.count)

    def player_turns(self, player1, player2):
        turn = self.player_check()
        if turn == 1:
            player = player1
            other_player = player2
            self.game(player, other_player)
        else:
            player = player2
            other_player = player1
            self.game(player, other_player)


if __name__ == "__main__":
    methods = game_methods()
    methods.player_turns(player1, player2)
