# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from_user = float(input("Введите число: "))

import math


from_user = str(
    input("Введите точность числа '兀' (например 0,001): "))
len_show = len(str(from_user).split('.,')[-1])
print(f'兀 = {str(math.pi)[:len_show]}')
