# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

from_user = int(input("Введите число: "))
i = 2
prime_numbers = []
while i <= from_user:
    if from_user % i == 0:
        prime_numbers.append(i)
        from_user //= i
    else:
        i += 1
print(f"Простые множители числа: {prime_numbers}")
