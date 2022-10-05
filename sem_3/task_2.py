# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


array_size = int(input("Введите сколько чисел должно быть в списке: "))
numbers = []
multiplied = []

for i in range(array_size):
    numbers.append(randint(1, 10))
print(f"Созданный список -> {numbers}")

if array_size % 2 == 0:
    for i in range(int(array_size / 2)):
        multiplied.append(numbers[i] * numbers[-i - 1])
else:
    for i in range(int(array_size / 2 + 1)):
        multiplied.append(numbers[i] * numbers[-i - 1])

print(f"Произведение пар чисел списка -> {multiplied}")
