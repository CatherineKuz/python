__author__ = 'Кузьмина Екатерина Алексеевна'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

number = int(input('Введите целое число: '))
while number != 0:
    print(number % 10)
    number = number // 10



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = b
b = a
a = c
print("Меняем их местами:")
print("Первое число равно " + str(a))
print("Второе число равно " + str(b))


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Сколько вам лет?'))
if age > 18:
    print('Добро пожаловать во взрослую жизнь!')
else:
    print('Малолеткам вход запрещен')