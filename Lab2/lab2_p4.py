# 4. Write a Python function that returns True only if any two elements in a sorted list sum to a given value S.

def sum_to_five(inputList,S):
    result = False
    for j in range(len(inputList)):
        if result == False:
            for i in range(len(inputList)):
                if inputList[j] + inputList[i] == S:
                    result = True
                    break
                else:
                    result = False
    if result == True:
        print("True")
    else:
        print("False")


inputList = [1, 2, 4, 8, 10]
S = 6
sum_to_five(inputList,S)

inputList = [1, 2, 4, 8, 10]
S = 15
sum_to_five(inputList,S)