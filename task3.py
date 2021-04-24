# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn
n = int(input("Введите число n: "))
digit = str(n)
d1 = digit + digit
d2 = digit + digit + digit
result = n + int(d1) + int(d2)
print("Результат равен:", result)