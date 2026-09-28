print("КАЛЬКУЛЯТОР")

# Арифметика и Сравнение 
a = int(input("введите первое число"))
b = int(input("введите второе число"))
op = input("Выберите оператор (+, -, *, /, //, %, **, ==, !=, >, <, >=, <=): ")

if op == "+":
    summa = a + b
    print(summa)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
elif op == "//":
    print(a // b)
elif op == "%":
    print(a % b)
elif op == "**":
    print(a ** b)
elif op == "==":
    print(a == b)
elif op == "!=":
    print(a != b)
elif op == ">":
    print(a > b)
elif op == "<":
    print(a < b)
elif op == ">=":
    print(a >= b)
elif op == "<=":
    print(a <= b)
else:
    print("Неверный оператор")

# Логические операторы 
age = 23
isMarried = True
print(not age > 21)
print(not isMarried)
result = (5 == 5) and (7 > 6)
print(result)
result = (5 == 5) or (6 > 7)
print(result)

age = int(input("Ваш возраст: "))
if age < 1:
    print("Введен некоректный возраст")
elif age < 18:
    print("Вам доступны милодрамы и комедии")
elif age >= 18:
    print("Доступны фильмы 18+")
else:
    print("Я рыба")

# Принадлежность и Тождественность 
message = "Русский квас"
print("Русский" in message)
print("лимонад" not in message)
s = [1, 2, 3, 4, 5]
print(6 in s)
print(1 in s)

x = [1, 2, 3]
y = x
print(x is y)
x = [1, 2, 3]
y = [1, 2, 3]
print(x is not y)
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)