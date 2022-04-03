#ELEN 520 Lab 1A Problem 4

from io import StringIO


#list2 = ['test', 'test', 'test', 'test', 'test']
#list3 = []
#list4 = ['Alabama', 'California', 'South Carolina', 'Florida', 'California', 'Alabama', 'California']

def stringFreq(listInput):
    strFreq = []
    listInputStr = []
    list1 = ['alpha', 'beta', 'gamma', 'delta', 'alpha', 'gamma']

    for i in range(len(list1)):
        listInputidx = list1.index(list1[i])
        strFreq[i] = len(listInputidx)
        listInputStr[i] = list1.pop(0)
        # dictOut[i] = [(listInputStr,listInputidx)]

    for i in range(len(strFreq)):
        print(listInputStr[i + "Frequency: " + strFreq[i]])

#strInput = input("Input list of strings: ")
strInput = ['alpha', 'beta', 'gamma', 'delta', 'alpha', 'gamma']
stringFreq(strInput)