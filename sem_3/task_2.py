# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


array_size = int(input("Введите сколько чисел должно быть в списке: "))
numbers = []
for i in range(array_size):
    numbers.append(randint(1, 10))
print("Заданный список рандомных чисел:", numbers)
lst_multiplied = []
if len(numbers) % 2 == 0:
    i = 1
    while i <= array_size / 2:
        multiplied = numbers[i - 1] * numbers[-i]
        lst_multiplied.append(multiplied)
        i += 1
    print(lst_multiplied)
else:
    i = 1
    while i <= array_size / 2:
        multiplied = numbers[i - 1] * numbers[-i]
        lst_multiplied.append(multiplied)
        i += 1
    print(lst_multiplied)
