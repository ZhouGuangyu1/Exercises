# 能卓1801 周广渝 201808020844
# time 2019-3-22
# 求到n的奇数阶乘的和
# 递归实现

def fact(n):               #定义递归函数
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

n = eval(input("请输入奇数："))  #获取输入值



def multifact(n):      #定义递归求和函数

   
    
    cout = 0      #求和初始值
    for i in range(1,n+1,2):    #遍历1到n的奇数
        cout = cout+fact(i)     #利用fact()求出每个奇数的阶乘，求和
    

    print("1到{}的奇数阶乘求和为{}".format(n,cout))          #打印输出



multifact(n)         #函数调用
    
