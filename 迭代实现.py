# 求到n的奇数阶乘的和
# 迭代实现
try:  #异常检测，防止用户输入非数字导致崩溃
    n = int(abs(eval(input("请输入奇数："))))    #接收输入

    def multifact(n):
        
        while n%2 != 1:
            n = int(abs(eval(input("你的输入不是奇数，请重新输入奇数："))))    #接收输入
    #用while循环让用户输入奇数为止
            
        cout,fact = 1,0     #cout为阶乘初始值，fact为和的初始值
        
        for i in range(1,n+1,2):    #遍历从1到N的奇数
            for c in range(1,i+1):  #遍历每个奇数的阶乘
                cout = cout*c       #计算阶乘
            fact = fact + cout      #阶乘求和
            cout = 1
        print("1到{}的奇数阶乘的和是：{}".format(n,fact))  #打印输出
        
    multifact(n)     #函数调用
except:
    print("你的输入值不是数字")







