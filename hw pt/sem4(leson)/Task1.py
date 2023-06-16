import random
def change_el (num, ind):
   return num[:ind]+ (random.randint(10,100), )+ num[ind+1:]
num=tuple(random.randint(1,10) for _ in range (10))
print(num)
ind=4
num=change_el(num,ind)
# m= tuple(random.randint(10,100), )
# nume= num[:5]+ m+ num[6:]
print(num)