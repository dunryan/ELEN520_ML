# ELEN 520 Lab 1 Problem 1

import random 

randNum = random.randint(1,20)

i = 0
while i < 3:
    guess = input("Guess an integer from 1 to 20: ")
    if guess == randNum:
        print("You guessed it!")
        success = True
    else:
        print("Sorry, you did not guess the number.")
        success = False
        i += 1
if success == False:
    print("The correct number was " + str(randNum) + ".")
    

