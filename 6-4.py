txt = input("请输入字符串：")
dict = {}
for i in txt:
    dict[i] = dict.get(i,0)+1
items = list(dict.items())
items.sort(key=lambda x:x[1],reverse=True)
print("{0:<10}{1:>5}".format("字符：","次数："))
for n in range(len(dict.keys())):
    i,count = items[n]
    print("{0:<10}{1:>5}".format(i,count))





