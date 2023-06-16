import math
from math  import*

num = int(input("количество элементов :"))
sl = [int(input()) for i in range(num)]
neednum = int(input("какое число нужно найти :"))
sp=[abs(neednum-i) for i in sl]
m=sp.index(min(sp))
print(sl[m])
