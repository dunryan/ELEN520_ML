import time
def dictRemove(userRemove,dict1):

    dict1Keys = dict1.keys()

    if userRemove not in ['1', '2', '3']:
        testString = userRemove
    else:
        testStringSet = ["Hamlet", "Alice's Adventures in Wonderland", "The Catcher in the Rye"]
        testString = testStringSet[int(userRemove)-1]

    if testString in dict1Keys:
        dict1.pop(testString)
        print("The key '" + testString + "' exists in the current dictionary and has been removed.\n")
        print("Updated dictionary: \n")
        print(dict1)
    else:
        print("The key '" + testString + "' does not exist in the dictionary.")

dict1 = {"Moby Dick": "Herman Melville", "Hamlet": "William Shakespeare", "The Catcher in the Rye": "J. D. Salinger", "The Odyssey" : "Homer"}
print("Dictionary in current state: \n")
time.sleep(1)
print(dict1)
print("\n")
time.sleep(1)
userRemove = input("Choose the key to remove from the dictionary: \n1) Hamlet \n2) Alice's Adventures in Wonderland \n3) The Catcher in the Rye\nInput string or integer of key here: ")
dictRemove(userRemove,dict1)
