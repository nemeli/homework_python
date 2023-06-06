num = int(input("количество элементов :"))
sl = [int(input()) for i in range(num)]
# for i in range(num):
#     sl.append(int(input()))
neednum = int(input("какое число нужно найти :"))
# for i in sl:
#     if i==neednum:
#         count+=1
count=len([i for i in sl if i ==neednum] )
print(f"Нужное число встречается {count} раз")
