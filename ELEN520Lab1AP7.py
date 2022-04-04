def iselement(caseTest):

    if caseTest == 'a':
        list1 = [10, 20, 30, 40]
        list2 = [10, 20, 30, 40]
    elif caseTest == 'b':
        list1 = [10, 20, 30, 40]
        list2 = [70, 80]
    elif caseTest == 'c': 
        list1 = ['apple', 'grapes', 'blueberries', 'oranges']
        list2 = ['bananas', 'oranges', 'tomatoes']
    elif caseTest == 'd':
        list1 = ['apple', 'grapes', 'blueberries', 'oranges']
        list2 = ['bananas', 'figs', 'tomatoes']
    
    if bool(set(list1) & set(list2)):
        print("Common elements in sets: True")
    else:
        print("Common elements in sets: False")

print("Logical test for any elements in array.\n")
print("Cases to choose from: \n")
print("Case a: \nlist1a = [10, 20, 30, 40]\nlist2a = [10, 20, 30, 40]\n")
print("Case b: \nlist1b = [10, 20, 30, 40]\nlist2b = [70, 80]\n")
print("Case c: \nlist1c = ['apple', 'grapes', 'blueberries', 'oranges']\nlist2c = ['bananas', 'oranges', 'tomatoes']\n")
print("Case d: \nlist1d = ['apple', 'grapes', 'blueberries', 'oranges']\nlist2d = ['bananas', 'figs', 'tomatoes']\n")

validEntry = False
while validEntry == False:
    caseTest = input("Input case letter here: ")
    if caseTest in ['a', 'b', 'c', 'd']:
        validEntry = True
    print("Invalid input, enter case letter, [ex: 'a']\n")

iselement(caseTest)
