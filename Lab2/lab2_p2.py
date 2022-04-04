# 2. Write a Python function that checks whether a passed string is palindrome or not.Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward

def palindrome_test(inputStr):

    if caseTest == 'a':
        inputStr = 'Was it a car or a cat I saw'
    elif caseTest == 'b':
        inputStr = 'Mom'
    elif caseTest == 'c': 
        inputStr = 'Able was I ere I saw Elba'
    elif caseTest == 'd':
        inputStr = 'A tin mug for a jar of gum Nita'

    outputStr1 = ''
    outputStr2 = ''
    for i in range(len(inputStr)):
        idx1 = len(inputStr) - i 
        if inputStr[idx1-1] != ' ':
            outputStr1 = outputStr1 + inputStr[idx1-1]
    for i in range(len(inputStr)):
        if inputStr[i] != ' ':
            outputStr2 = outputStr2 + inputStr[i]

    if outputStr1.lower() == outputStr2.lower():
        print("Phrase is a palindrome!")
    else:
        print("Phrase is not a palindrome :(\n")
    print("Input string: " + inputStr + "\n")
    print("Output string forward: " + outputStr1.lower() + "\n")
    print("Output string reversed: " + outputStr2.lower() + "\n")

# Prompt user for string input
print("Test cases for palindromes:\n")
print("Cases to choose from: \n")
print("Case a: \n'Was it a car or a cat I saw'\n")
print("Case b: \n'Mom'\n")
print("Case c: \n'Able was I ere I saw Elba'\n")
print("Case d: \n'A tin mug for a jar of gum Nita'\n")

validEntry = False
while validEntry == False:
    caseTest = input("Input case letter here: ")
    if caseTest in ['a', 'b', 'c', 'd']:
        validEntry = True
    else:
        print("Invalid input, enter case letter, [ex: 'a']\n")

print("** Testing Palindrome **")
print("***************")
palindrome_test(caseTest)