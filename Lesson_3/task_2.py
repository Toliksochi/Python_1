# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

N = int(input("Введите длину массива: "))
R = int (input("Введите верхнюю границу массива:"))
list_1 = [random.randint(1, R) for i in range(N)]
print(list_1)
X = int(input("Введите нужное число "))
index_element = 0
min_element = abs(X - list_1[0])
for i in range(1, N):
    element_A = abs(X -list_1[i])
    if element_A < min_element:
        min_element = element_A
        index_element = i

print(f"Самый близкий по величине элемент к заданному числу {list_1[index_element]}")