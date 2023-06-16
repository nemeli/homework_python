import random
l=10
num=set(random.randint(1,20) for i in range(l))
print(num,l-len(num))