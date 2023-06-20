def sum_2num(num1,num2):
    if num2<=0:
        return num1
    return sum_2num(num1+1,num2-1)

num1=int(input("Введите первое число  "))
num2=int(input("Введите второе число  "))
print(f"сумма двух чисел равна  {sum_2num(num1,num2)}")