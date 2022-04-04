# 5.  Write a Python script to check whether a given key already exists in a dictionary.
#  Test cases:
# dict1 = {"Moby Dick": "Herman Melville", "Hamlet": "William Shakespeare", "The Catcher in the Rye": "J. D. Salinger", "The Odyssey" : "Homer"}
#  check for the following keys:
# "Hamlet"
# "Alice's Adventures in Wonderland"
# "The Catcher in the Rye"

testString = ["Hamlet", "Alice's Adventures in Wonderland", "The Catcher in the Rye"]

dict1 = {"Moby Dick": "Herman Melville", "Hamlet": "William Shakespeare", "The Catcher in the Rye": "J. D. Salinger", "The Odyssey" : "Homer"}

dict1Keys = dict1.keys()

for i in range(len(testString)):
    if testString[i] in dict1Keys:
        print("The key '" + testString[i] + "' exists in the dictionary.")
    else:
        print("The key '" + testString[i] + "' does not exist in the dictionary.")



