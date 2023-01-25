from random import randint


def randomCheck():
    random_number = randint(1, 6)
    print("Number obtained by player = ", random_number)
    return random_number


def optionCheck():
    option = randint(0, 2)
    return option
