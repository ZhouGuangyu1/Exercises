def judge(b):
    
    if len(set(b)) != len(b):  
        print("True")
    else:
        print("列表没有相同元素")
    print(b)    #检查原列表是否改变
b = input("请输入参数列表：")
judge(b)

#利用集合去重后的长度与原列表长度来判断
#长度不等则有相同元素被去掉，得知有元素出现不止一次


"""
#test
judge([1,2,3,4,5,4,3,"w","q",2,1])
judge([1,2,3,4,5])

"""

#下面是不用集合去重来实现目的：

"""

def fun1(ls):
    for i in ls:
        if ls.count(i) > 1:
            print("True")
            break

    print(ls)

#test
fun1([1,2,3,4,5,4,3,"w","q",2,1])
fun1([1,2,3,4,5])

"""



