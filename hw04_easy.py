# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

my_list = [1, 2, 3, 4]
new = [el**2 for el in my_list]
print(new)



# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit1 = ["apple", "banana", "grapes"]
fruit2 = ["banana", "pineapple", "grapes", "pear"]
fruit_new = [el for el in fruit1 if el == el in fruit2]
print(fruit_new)

fruit_new = list(set(fruit1)&set(fruit2))
print(fruit_new)



# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

my_list = [1, 2, 3, 4, 5, 6, -3, -7, 8, 9, 12, 0]
new = [el for el in my_list if el > 0 and el%3 == 0 and el%4 != 0]
print(new)



