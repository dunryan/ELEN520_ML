# ELEN 520 Lab 1A Problem 3
import time

list1 = [1, 2, 3, 4, 5, 6] #   output: 2, 3, 4, 5, 6, 1
list2 = [10, 100, 1000, 10, 100, 1000] # output: 100, 1000, 10, 100, 1000, 10
list3 = [5, 15, 20, 25, 30, 35, 40, 45, 50]# output: 15, 20, 25, 30, 35, 40, 45, 50, 5

output1 = []
output2 = []
output3 = []

for i in range(len(list1)):
    output1[i] = list1.pop(1)

print(output1)

for i in range(len(list2)):
    output2 = list2.pop(1)
    print(output2)

for i in range(len(list2)):
    output3 = list3.pop(1)
    print(output3)

time.sleep(5)