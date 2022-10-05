# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

array_size = int(input("Введите сколько чисел должно быть в списке: "))
float_numbers = []

for i in range(array_size):
    float_numbers.append(round(uniform(1, 10), 2))
print("Список вещественных чисел", float_numbers)

for i in range(array_size):
    float_numbers[i] = float_numbers[i] - int(float_numbers[i])
float_numbers.sort()
dif_numbers = float_numbers[-1] - float_numbers[0]
print(f"Разница между максимальным и минимальным значением дробной части элементов: {round(dif_numbers, 2)}")
