# Задайте список из N элементов,
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

a = int(input("Введите число N: "))
b = (a * -1) -1
lst = []
i = b
while i <= a -1:
    i += 1
    lst.append(i)
print("Список от -N до N", lst)
f = open('pos_num.txt', 'r')
line =[]
for i in f:
    line.append(i)
f.close()
print("Позиции в .txt файле", line)
multiplication = lst[int(line[0])] * lst[int(line[1])] * lst[int(line[2])]
print("Результат произведения чисел", lst[int(line[0])], lst[int(line[1])], lst[int(line[2])], "будет", multiplication)