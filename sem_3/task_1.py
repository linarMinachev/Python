# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


len_array = int(input("Введите сколько чисел должно быть в списке: "))
numbers = []
sum_elements = 0

for i in range(len_array):
    numbers.append(randint(1, 10))
for val in numbers[1::2]:
    sum_elements += val

print(f"Созданный список -> {numbers}\nСумма этих элементов -> {sum_elements}")
