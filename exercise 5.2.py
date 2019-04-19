# File name: exercise 5.2
# Date: 2019-03-01 
# Version: 1.0
# Author: Zhou Guangyu
def isOdd(num):
    if type(num) ==type(2):
        if num/2 - int(num/2) == 0:
            print("False")
        else:
            print("True")
    else:
        print("参数不为整数，请调试")

# test
isOdd(6)
isOdd(6+9j)
isOdd("6")
isOdd(1)
            
