from math import *
from random import *


print("1Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n елок. Изображение одной елки имеет размер 4×9 символов, между двумя соседними елками также имеется пустой (из пробелов) столбец.")
print("Разрешается вывести пустой столбец после последней елки. Для упрощения рисования скопируйте елку из примера в среду разработки. Елки должны простоложиться горизонтально.")
print()
print()
try:
    n=int(input("vali 1-9 palju tahad näha kuuske? "))
    if n<1 or n>9:
        print("Vale vahemik")
except:
    print("Vale andmetüüp")
x=0
for x in range(4):
    for e in range(n):
        if x == 0:
            print("     /V\     ", end="")
            
        elif x == 1:
            print("    / V \    ", end="")
        
        elif x == 2:
            print("   / V V \   ", end="")      
        
        elif x == 3:
            print("  /VV V VV\  ", end="")
    print("")
  


print("2.Перемножить все не чётные значения в диапазоне от 0 до введенного пользователем числа(R)")
R=int(input("kirjuta üles täisarv: "))
p = 1
for i in range(1, R, 2): p *= i
print(p)
print()


print("3.Дано N чисел. Найти количество положительных чисел среди них; N рандомное число")
p=0
N=randint(1,100)
for i in range(N):
    A=randint(-1000,1000)
    for i in range(1):
        print(A)
    if A>0:
        p+=1
print("positiivsed numbrid", p)
print()



print("4. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).")
try:
    a=int(input("sisestage number: "))
except:
    print("Vale andmed")
b=0
c=0
while a>0:
    if a%2==0:
        b+=1
    else:
        c+=1
    a=a//10
print("paarisarvud", b)
print("paarituid numbreid", c)
print()



print("5.Найти сумму ряда чисел от A до B. Полученный результат вывести на экран")
b=int(input("sisestage teine ​​number: "))
n=int(input("sisesta viimane number: "))
i=1
s=0
while i<=n:
    s=i+s
    i=i+s 
print("arvude summa alates",i,"kuni",b,"=", (s))