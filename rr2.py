#Условные конструкции

#if условие:
    #болк кода, который выполняется, если условие = True
#следующий блок кода
x=4
if x>5:
    print("x>5")

buh=45

money=int(input("Сколько денег с собой? "))
if money>=buh:
    print("Вы можете купить булку")

#Оператор if-else
#if условие:
    #блок кода 1, волниться, если условие=True
#else:
    #блок кода 2, выполниться если предыдущее условие=False

if money>=buh:
    print("Вы можете купить булку")
else:
    print("Вы не можете купить булку")

x=15
if x>10:
    print("x>10")
    if x>20:
        print("x>20")
    else:
        print("10<x>/=20")
else:
    print("x</=10")

language="английский"
language="русский"
daytime="утро"
if language=="английский":
    print("English")
    if daytime=="утро":
        print("Good morning")
    else:
        print("Good evening")
else:
    if daytime=="morning":
        print("Доброе утро")
    else:
        print("Добрый вечер")

#Конструкция if-elif-else
#if - проверяет первое условие
# elif - проверяет следующие условия, если предыдуще==false
# else - выполняет блок кода, ели все предыдущие были ложны
 
# if условие1:
#   блок кода 1
# elif условие2:
#   блок кода 2
# elif условие3:
#   блок кода 3
# else:
#   блок кода 4  

x=8
if x>10:
    print("x>10")
elif x>5:
    print("5<x или x=10")
elif x>0:
    print("x>0 или 5>/=x")
else:
    print("x>5 или x=0")

age=int(input("Ваш возраст: "))
if age<1:
    print("Введен некоректный возраст")
elif age<18:
    print("Вам доступны милодрамы и комедии")
elif age>=18:
    print("Доступны фильмы 18+")
else:
    print("Я рыба")

x=6
if x>=6:
    print("Привет")
else:
    print("Пока")
print("Нет привет")

#Тернарный оператор
x=10
result="x больше 5" if x>5 else "x не больше 5"
print(result)

print("Введите первую и последнюю буквы русского алфавита")
first_let=input()
second_let=input()
if (first_let=="а" or first_let=="А") and (second_let=="я" or second_let=="Я"):
    print("Верно")
else:
    print("Неверно")

#if x>=0 and x<100  =>  if o<= x <100

#Напишите программу, которая запрашивает у пользователя число и выводит, является ли оно чётным или нечётным.
x=int(input("Введите число "))
if x%2==0:
    print("Оно четное")
else:
    print("Оно не четное")
#Запросите два числа и выведите наибольшее из них.
first=int(input("Введите первое число"))
second=int(input("Введите второе число"))
if first>second:
    print(first)
elif first==second:
    print("Эти числа равны")
else:
    print(second)
#Определите знак введённого числа.
x=int(input("Ведите число"))
if x<0:
    print("Оно отрицательное")
elif x==0:
    print("Оно равно 0")
else:
    print("Оно положительное")




