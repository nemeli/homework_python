# Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

sum=int(input("Введите сумму чисел  "))
proi=int(input("Введите произведение чисел  "))
flag=1
for i in range(1000):
    for j in range(1000):
        if i+j==sum and i*j== proi:
            print(f"Первое число {i} Второе число {j}")
            flag=0
            break
    if flag==0:
        break
if flag==1:
    print("Числа введены не верно")   
