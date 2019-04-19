# File name: exercise 5.3
# Date: 2019-03-01 
# Version: 1.0
# Author: Zhou Guangyu
def isNUM(cha):
    if type(cha) == type(3) or type(cha) == type(1.2):
        print("True")
    elif type(cha) == type(3+6j):
        print("True")
    else:
        print("False")

# test
isNUM(9.2)
isNUM(9)
isNUM(9-2j)
isNUM("9")
