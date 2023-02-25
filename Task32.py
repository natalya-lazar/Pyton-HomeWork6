# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint
start, stop = [int(i) for i in input("Enter range: ").split()]
list_num = [randint(-10, 10) for i in range(randint(10, 20))]
print(list_num)
range_list = [i for i in range(len(list_num)) if list_num[i] >= start and list_num[i] <= stop]
print(range_list)