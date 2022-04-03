# ELEN 520 Lab 1A Problem 2
import time
def word_score(userWord):

    score = {"a": 1, "b": 2, "c": 3, "d": 1, "e": 2, "f": 2,
            "g": 3, "h": 4, "i": 4, "j": 5, "k": 4, "l": 3,
            "m": 1, "n": 1, "o": 1, "p": 10, "q": 8, "r": 1,
            "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 9,
            "y": 8, "z": 10}
    keys = list(score.keys())
    scoreTrack = 0
    for i in range(len(userWord)):
        idx = keys.index(userWord[i])
        scoreTrack = scoreTrack + score[userWord[i]]
    print("word = " + userWord + ", score = " + str(scoreTrack))
    time.sleep(5)

userInput = input("Please input the word to score: ")
word_score(userInput)



