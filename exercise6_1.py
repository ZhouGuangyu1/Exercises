import string   #引入string模块
import random
     
ls = list(string.ascii_letters + string.digits)
#创建包含所有字母(大写或小写)和0—9的数字元素的列表ls

"""
另一种实现含所有字母和数字元素的列表方法
ls = []
for i in range(48,58):
    ls.append(chr(i))
用内置函数chr()他们对应的unicode编码转换成字符串添加到空列表

"""
for i in range(100):
    lt = []
    while len(lt) < 8:
        lt.append(random.choice(ls))
   
    password = "".join(lt)
        
    print("密码{}：{}".format(i+1,password))   # i+1符合人类计数习惯

        

