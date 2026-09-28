print (2+4)
print("насти")

print (2+4)
print("насти")

if 1<2:
    print("hello")
else:
    print("f")

#регистрозависимость
#  Print("папа")
#Print неправильно

# - строчный комментарий
print("hdhd") #функция вывода данных в консольных
''' БЛОЧНЫЕ КОММЕНТАРИИ '''
""" Блочные комментарии """

#print - выводы информации на консоль (терминал)
print ("Анна")
print ("Анна",19,"Любит петь")

name = input("Введите имя")
print(name)


''' False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield '''

# = знак присвоения
name = "Настя"

#camel case
userName="Анастасия"

#underscore notatoin
user_name="Анастасия"

#две разные переменные
Age=24
print(Age)

age=15
print(age)

#типы данных

#Чмсловые типы данных
'''
int- Целые числа x=5
float - вещественный тип данных(число с плавающей точкой) y=5,6

'''

#Текстовые типы данных
'''
str - Строка, состроящие из символов, заключенные в одинарные или двойные кавычки
name="Фил"
'''
'''bool - Логические значения (True - истина, False - ложь)

is_activate=True
'''
#Списки и коллекции

#None
'''
NoneType- особый тип данных, который представляет отсутствие значения
z=None
'''

z=2
x=3.4
is_activate=False
d=None

#2-10
a=0b11
print(a)
b=0b1011
print(b)
c=0b100001
print(c)

#8-10
a1=0o7
a2=0o11
print(a1,a2)

#16-10
a3=0x0A
print(a3)

x=10
y=str(x) #число стало строкой
z=float(x) #число стало в виде вещ типа
print(x,y,z)
s=2
u=7
sum=s+u
print(sum)
#Напишите программу, которая запращивает имя пользователя и выводит приветствие: "Привет,[имя]!"
#name = input("введите имя")
#print("привет", name"!")

#Пользователь вводит два целых числа. Программа выводит их сумму.
a = int(input("введите первое число"))
b = int(input("введите второе число"))
print(a+b)
summa=a+b
print(summa)

#Введите длину и ширину прямоугольника(числа с плавающей точкой). Выведите его площадь и периметр.
b_y=int(input("введите год рождения"))
a_y=int(input("введите текущий год"))
#Введите два числа. Поменяйте их местами и выведите результат (без использования третьей переменной).
#Картежный способ
a= 10
b= 20
print(f"До обмена: a = {a}, b = {b}")
a, b = b, a
print(f"После обмена: a = {a}, b = {b}")

#Количественные числа complex
complexlexNumber=1+2
print(complexlexNumber)
''' Управляющие последовательности в строке

# Строка может содержать ряд специальных символов - управляющих последовательностей. 

# Некоторые из них:

# \\: позволяет добавить внутрь строки слеш

# \': позволяет добавить внутрь строки одинарную кавычку

# \": позволяет добавить внутрь строки двойную кавычку

# \n: осуществляет переход на новую строку

# \t: добавляет табуляцию (4 отступа)

# '''
text="Сообщение:\n\"Hello, my frinds\""
print(text)
text1="Сообщение:\n\"Hello, my frinds\""
print(text1)

#print("gisi",end="hjihi ")
#print("dsjd")

#Операторы в програмирование

#Арифмитические операторы

# + - / *
# // -целочисленное деление
# % - деление с остатком
# ** -возведение в степень

print(4+5)
print(4-5)
print(6*8)
print(12/5)
print(12//5)
print(25%3)
print(2**2)

#Операции направления

#** - справо налево
#* / // % - слева направо
#+- - слева направо
number= 3 + 4 * 5 ** 2 + 7
#1 шаг
#5**2=25
#2 шаг
#25*4=100
#3 шаг
#100+3=103
#4 шаг
#103+7=110
print(number)

number= (3 + 4) * (5 ** 2 + 7)
print(number)

#Арифмитические операции с присвоением

#+=
#-=
#/=
#*=
#//=
#%=
#**=

number=10
number+=5
number-=5
number/=5

#Округление  round
first_num=2.0001
sec_number=5
third=first_num/sec_number
print(third)
print(round(2.0001+0.1))
print(round(2.0001+0.1,2))

print(round(4.67859940+9.7799,3))

#Операторы сравнения
print(2>3) #больше
print(3==3) #равно
print(2!=9) #не равно
print(3>=3) #больше или равно
print(3<4) #меньше
print(4<=5) #меньше или равно

#Логические операции

# and - два истинна обязательно
# or - хотя бы одно истинно
# not - инверсия(например, было ложно столо правдой)

age=23
isMarried= True
print(not age >21)
print(not isMarried)

result= (5==5) and (7>6)
print(result)

result= (5==5) or (6>7)
print(result)

# значение in набор_значений

message="Русский квас"
print("Русский" in message)

print("лимонад" not in message)

s=[1,2,3,4,5]
print(6 in s)
print(1 in s)

#Операторы торждественности
x=[1,2,3]
y=x
print(x is y)

x=[1,2,3]
y=[1,2,3]
print(x is not y)

x=[1,2,3]
y=[1,2,3]
print(x == y)

x=[1,2,3]
y=[1,2,3]
print(x is y)

name="Иван"
age=25
print(age)
height=1.75
print(height)
is_student= True
nothing= None
Age= 20
print(Age)
age= 10
print(age)

a=10
