# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введите X: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

print((not (x or y or z)) == (not x and not y and not z))