# ELEN 520 Lab 1A Problem 3
import time

list1 = [1, 2, 3, 4, 5, 6] #   output: 2, 3, 4, 5, 6, 1
list2 = [10, 100, 1000, 10, 100, 1000] # output: 100, 1000, 10, 100, 1000, 10
list3 = [5, 15, 20, 25, 30, 35, 40, 45, 50]# output: 15, 20, 25, 30, 35, 40, 45, 50, 5

output1 = [0] * len(list1)
output2 = [0] * len(list2)
output3 = [0] * len(list3)

tempList = list1[:]
for i in range(len(list1)):
    if len(tempList) > 1:
        output1[i] = tempList[1]
        tempList.pop(1)
    else:
        output1[i] = tempList[0]
        tempList.pop(0)

print("Output for list1 stripped each second index: ")
print(output1)

tempList = list2[:]
for i in range(len(list2)):
    if len(tempList) > 1:
        output2[i] = tempList[1]
        tempList.pop(1)
    else:
        output2[i] = tempList[0]
        tempList.pop(0)

print("Output for list2 stripped each second index: ")
print(output2)

tempList = list3[:]
for i in range(len(list3)):
    if len(tempList) > 1:
        output3[i] = tempList[1]
        tempList.pop(1)
    else:
        output3[i] = tempList[0]
        tempList.pop(0)

print("Output for list3 stripped each second index: ")
print(output3)

time.sleep(5)