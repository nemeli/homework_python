one=("A","E","I","O","U","L","N","S","T","R","А","В","Е","И","Н","О","Р","С","Т")
two=("D","G","Д","К","М","П","У")
three=("B","C","M","P","Б","Г","Ё","Ь","Я")
four=("F","H","V","W","Y","Й","Ы")
five=("K","Ж","З","Х","Ц","Ч")
eight=("J","X","Ш","Э","Ю")
then=("Q","Z","Ф","Щ","Ъ")
s={one:1,two:2,three:3,four:4,five:5,eight:8,then:10}
m=str(input())
m=m.upper()
word=[]
word.extend(m)
count=0
for i in word:
    if i in one:
        count+=1
    elif i in two:
        count+=2
    elif i in three:
        count+=3
    elif i in four:
        count+=4
    elif i in five:
        count+=5
    elif i in eight:
        count+=8
    elif i in then:
        count+=10

        


print(count)