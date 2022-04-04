# Write a python function called string_rev to reverse a string.

def string_rev(inputStr):
    outputStr = ''
    for i in range(len(inputStr)):
        idx = len(inputStr) - i 
        outputStr = outputStr + inputStr[idx-1]
    print("Input string: " + inputStr + "\n")
    print("Output string: " + outputStr + "\n")

# Prompt user for string input
strInput = input("Enter string to reverse: \n")
print("** Reversing **")
print("***************")
string_rev(strInput)