# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
from math import *
num=int(input("Введите число  "))
step=0
i=0
while step<num:
    step=pow(2,i)
    i+=1
    if step<num:
        print(int(step),end=" ")