# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input("Введите номер четверти: "))

if quarter_number == 1:
    print("x > 0; y > 0")
elif quarter_number == 2:
    print("x < 0; y > 0")
elif quarter_number == 3:
    print("x < 0; y < 0")
elif quarter_number == 4:
    print("x > 0; y < 0")
else:
    print("Вы вышли за пределы четвертей")
    