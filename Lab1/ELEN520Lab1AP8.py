 # Write a Python program to print the numbers of a specified list after removing even numbers from it.

list1 = [10, 20, 35, 27, 28]
listTemp = list1[:]

for i in range(len(list1)):
    if (list1[i] % 2) == 0:
        idx = listTemp.index(list1[i])
        listTemp.pop(idx)

print("List 1 without even numbers: ")
print(listTemp)

list2 = [10, 20, 35, 27, 28, 100, 200, 300, 15, 17, 29]
listTemp = list2[:]

for i in range(len(list2)):
    if (list2[i] % 2) == 0:
        idx = listTemp.index(list2[i])
        listTemp.pop(idx)

print("List 2 without even numbers: ")
print(listTemp)
