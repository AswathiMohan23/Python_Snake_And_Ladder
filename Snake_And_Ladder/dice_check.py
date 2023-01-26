from random import randint


class dice_check:

    def randomCheck(self):
        random_number = randint(1, 6)
        return random_number

    def optionCheck(self):
        option = randint(0, 2)
        return option
