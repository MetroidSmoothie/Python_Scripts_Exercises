# randint() Module:
#       Creates and maps random numbers for specified arguments
#       randint(x,y) will return random int in range that is defined in parenthesis

import random

"""
while True:
    user_guess = int(input("Guess a number between 1 and 10: "))
    randG = random.randint(1,10)
    if randG != user_guess:
        print(f" Wrong guess the number is {randG}")
    else:
        print("You got it!")
"""

# THROW THE DICE __________________________

# import random

print("\nWelcome to throw dice!")
input("Press any key to throw the first dice...")
firstDice = random.randint(1,6)
input("\nPress any key to throw the second dice...")
secondDice = random.randint(1,6)

print("\nThe result of your roll is {},{}".format(firstDice, secondDice))
