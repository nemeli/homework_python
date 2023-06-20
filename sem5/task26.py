num1=int(input("Введите первое число  "))
num2=int(input("Введите второе число  "))

def degree (num_1,num_2):
    print(num_1,num_2)
    if num_2<=1:
        return(num_1)
    return degree(num_1*num1,num_2-1)

print(degree(num1,num2))