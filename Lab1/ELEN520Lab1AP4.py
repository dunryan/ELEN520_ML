#ELEN 520 Lab 1A Problem 4

from io import StringIO

#list1 = ['alpha', 'beta', 'gamma', 'delta', 'alpha', 'gamma']
#list2 = ['test', 'test', 'test', 'test', 'test']
#list3 = []
#list4 = ['Alabama', 'California', 'South Carolina', 'Florida', 'California', 'Alabama', 'California']

def stringFreq(listInput):

    if listInput == '1':
        list1 = ['alpha', 'beta', 'gamma', 'delta', 'alpha', 'gamma']
    elif listInput == '2':
        list1 = ['test', 'test', 'test', 'test', 'test']
    elif listInput == '3': 
        list1 = []
    elif listInput == '4':
        list1 = ['Alabama', 'California', 'South Carolina', 'Florida', 'California', 'Alabama', 'California']

    print("************** Processing *******************")
    output = dict((i,list1.count(i)) for i in list1)
    if output:
        print("Result: ")
        print(output)
    else:
        print("Empty array provided.")

print("Output frequency of elements in array\n")
print("Cases to choose from: \n")
print("Case 1: \nlist1 = ['alpha', 'beta', 'gamma', 'delta', 'alpha', 'gamma']\n")
print("Case 2: \nlist2 = ['test', 'test', 'test', 'test', 'test']\n")
print("Case 3: \nlist3 = []\n")
print("Case 4: \nlist4 = ['Alabama', 'California', 'South Carolina', 'Florida', 'California', 'Alabama', 'California']\n")

validEntry = False
while validEntry == False:
    listInput = input("Input case number here: ")
    if listInput in ['1', '2', '3', '4']:
        validEntry = True
    else:
        print("Invalid input, enter case number, [ex: '1']\n")

stringFreq(listInput)