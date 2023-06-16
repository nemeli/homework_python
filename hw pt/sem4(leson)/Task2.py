m=10
n=5
# def chas(m,n):
#     lis=[]
#     lis.append(m+n)
#     lis.append(m-n)
#     lis.append(m*n)
#     lis.append(m//n)
#     return lis
def calc (m,n):
    return m+n,m-n,m*n,m//n
# lis= chas(m,n)
sum,raz,um,de=calc(m,n) # расспаковка картежа упакованного автоматически методом
# res=calc(m,n) # данный метод выводит картеж
# print(f"сумма {lis[0]}, разность {lis[1]}, произведение {lis[2]}, частное {lis[3]}")
print(sum,raz,um,de)