from matplotlib.cbook import strip_math


class validString:
    def __init__(self,strInput):
        self.__strInput = strInput

    def isValidStr(self):
        strInput = self.__strInput
        if len(list(strInput))%2 != 0:
            return False
        for i in range(len(strInput)):
            if strInput[i] == '(' and strInput[i+1] != ')':
                return False
            elif strInput[i] == '[' and strInput[i+1] != ']':
                return False
            elif strInput[i] == '{' and strInput[i+1] != '}':
                return False
        return True

isValid = validString('{]')

print(isValid.isValidStr())
