import jieba
excludes = {"什么","一个","我们","那里","你们","如今","知道","说道","起来","姑娘","这里",\
            "他们","自己","众人","出来","一面","只见","没有","不知","这样","东西","就是",\
            "咱们","就是","怎么","太太","两个","不是","这个","进来","只得","听见",\
            "告诉","袭人","大家","不敢","这些","所以","回来","一时","鸳鸯","不好","姐姐",\
            "出去","二爷","的话","如此","心里","只是","不过","不能","过来","银子","今日","二人","还有","几个","答应","只管","这么","说话","一回","这话","外头","自然","今儿","打发","罢了","屋里","那些","听说"}
txt = open("红楼梦.txt","r",encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "老太太" or word == "奶奶":
        rword = "贾母"
    elif word == "丫头":
        rword = "黛玉"
    elif word == "老爷":
        rword = "贾源"
    elif word == "凤姐" or word == "凤姐儿":
        rword = "王熙凤"
    else:
        rword = word
    counts[rword] = counts.get(rword,0)+1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
print("{0:<10}{1:>5}".format("人物:","出现次数:"))
for i in range(20):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
