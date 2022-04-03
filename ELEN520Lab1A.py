# ELEN 520 Lab 1 Problem 1

import random 

randNum = random.randint(1,20)

i = 0
while i < 3:
    guess = input("Guess an integer from 1 to 20: ")
    if guess == randNum:
        print("You guessed it!")
    else:
        print("Sorry, you did not guess the number.")
        i += 1
    

