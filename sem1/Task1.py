# Найдите сумму цифр трехзначного числа.
nu = input('введите трехзначное число: ')
sum = 0
if len(nu) == 3:
    num = int(nu)
    for i in range(3):
        sum += num % 10
        num //= 10
    print(f'сумма цифр = {sum}')
else:
    print('число введено не корректно')