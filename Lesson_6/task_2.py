from random import randint

list = [randint(-10, 10) for i in range(20)]
print (list)
min_number = int(input("Введите минимальное число"))
max_number = int(input("Введите максимальное число"))
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)