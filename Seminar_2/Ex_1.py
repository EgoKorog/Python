# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

n = float(input('Введите число : '))
suma = 0
mult = 1

if n != int:
    n = n*1000000

while n > 0:
    digit = n % 10
    suma = round ((suma + digit))
    # mult = mult * digit
    n = n // 10
 
print ("Сумма:", suma)
