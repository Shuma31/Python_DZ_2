# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input("Введите число: "))
num = int(str(num).replace('.', ''))
print(num)
sum = 0

while num > 0:
    sum +=num%10
    num = num//10
print(sum)
