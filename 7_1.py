#-*- coding:utf-8 -*-
import os

s=["def","for","print","in","range","end"]
while True:
    fname = input("请输入文件名：")
    try:
        fo = open(fname,"rt",encoding="utf-8")
    except FileNotFoundError:
        print("文件不存在，请重输：")
    else:
        break
ls1 = []
for line in fo:
    ls2 = line.split()
    for i in ls2:
        if i not in s:
            ls1.append(i.upper())
        else:
            ls1.append(i)

fw = open("NewFile.py","w+",encoding="utf-8")
ls1 = " ".join(ls1)
fw.write(ls1)





fo.close()
fw.close()
print("操作已完成")



    
    
  



