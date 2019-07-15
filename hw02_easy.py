# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

fruit = ["яблоко", "банан", "киви", "арбуз"]
print(len(fruit))

for i in range(0, len(fruit)):
    print(i+1, '{:>10}'.format(fruit[i]))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

fruit1 = ["яблоко", "банан", "киви", "арбуз", "киви", "ананас"]
fruit2 = ["яблоко", "киви", "банан", "мандарин", "апельсин"]
i = 0
if fruit1[i] == fruit2[i]:
    fruit1.pop(i)
print(fruit1)

# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


numbers = [34, 25, 128, 111, 29, 32]
numbers_new = []
for i in numbers:
    if i % 2:
        numbers_new.append(i*2)
    else:
        numbers_new.append(i/4)
print(numbers_new)
