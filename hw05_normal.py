# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций, и импортированные в данный файл из easy.py

import hw05_easy as easy
import os
import sys

def open_dir(path):
    try:
        os.chdir(path)
    except OSError:
        print(f"Папки {path} не существует")
    else:
        print(f"Успешно попали в папку {path}")

if __name__=="__main__":
    print('1 - Перейти в папку')
    print('2 - Просмотреть содержимое текущей папки')
    print('3 - Удалить папку')
    print('4 - Создать папку')
    print('5 - завершить работу')
    command = input("Введите номер действия: ")
    if command == '1':
        new_path = input("Введите название папки, которую вы хотите открыть: ")
        open_dir(new_path)
    elif command == '2':
        easy.list_dir()
    elif command == '3':
        dir_name = input("Введите название папки, которую вы хотите удалить: ")
        easy.del_dir()
    elif command == '4':
        dir_name = input("Введите название папки, которую вы хотите создать: ")
        easy.make_dir()
    elif command == '5':
        sys.exit