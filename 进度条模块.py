import time
scale = 20
n = chr(9608)

for i in range(scale+1):
    a = n*i
    b = " "*(scale-i)
    c = (i/scale)*100
    print("\r{:^3.0f}%{}{}".format(c,a,b),end = "")
    time.sleep(0.1)
