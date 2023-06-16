import random
quan=int(input("введите количество кустов  "))
berr=list(random.randint(1,40) for i in range (quan))
print(berr)
maxim=0
for i in range (quan-2):
    if berr[i]+berr[i+1]+berr[i+2]>maxim:
        maxim=berr[i]+berr[i+1]+berr[i+2]
if berr[0]+berr[1]+berr[quan-1]>maxim:
    maxim=berr[0]+berr[1]+berr[quan-1]
if berr[0]+berr[-2]+berr[-1]>maxim:
    maxim=berr[0]+berr[-2]+berr[-1]
print(maxim)

