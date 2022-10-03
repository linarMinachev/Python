# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


len_array = int(input("Введите сколько чисел должно быть в списке: "))
numbers = []
for i in range(len_array):
    numbers.append(randint(1, 10))
i = -1
sum_elements = 0
while i < len(numbers)-1:
    i += 1
    if i % 2 != 0:
        sum_elements += numbers[i]
numbers_odd = numbers[1::2]
print(f"Созданный список -> {numbers}\nЭлементы на нечетных позициях -> {numbers_odd}\nСумма этих элементов -> {sum_elements}")
