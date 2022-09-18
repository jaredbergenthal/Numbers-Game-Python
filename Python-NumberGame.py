#import os
#os.makedirs(r'c:\temp\temp')


import random
import math

print("Welcome to My Number Guessing Game!")
print("You will have to guess a number between two numbers.... \nFor each wrong guess I will tell you if you need to go higher or lower")
lower = int(input("Enter Lower Limit:"))
 
# Taking Inputs
upper = int(input("Enter Upper Limit:"))



x = random.randint(lower, upper)
print("You've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!")


guess = int(input("Guess a number:"))
print("")
count = 0


while count < math.log(upper - lower + 1, 2):
    count = count + 1
    if x == guess:
        print("Congratulations! you did it in", count, "tries!")
        break
    # Once guessed, loop will break
    elif x > guess:
        print("You guessed too small! Guess Again")
        print("You have", round(math.log(upper - lower + 1, 2)) - count, "tries remaining")
        guess = int(input("Guess a number:"))
    elif x < guess:
        print("You Guessed too high!")
        print("You have", round(math.log(upper - lower + 1, 2)) - count, "tries remaining")
        guess = int(input("Guess a number:"))
                   
