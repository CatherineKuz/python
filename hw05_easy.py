# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

def make_dir(path):
    try:
        os.mkdir(os.path.join(os.getcwd(), path))
    except FileExistsError:
        print(f'Директория {path} уже существует')
    else:
        print(f'Директория {path} успешно создана')

def del_dir(path):
    try:
        os.rmdir(os.path.join(os.getcwd(), path))
    except OSError:
        print(f"Удалить директорию {path} не удалось")
    else:
        print(f"Успешно удалена директория {path}")



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir():
    folders = os.listdir(os.getcwd())
    print(folders)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(file_name):
    new_file = file_name + '.copy'
    try:
        shutil.copy(file_name, new_file)
    except OSError:
        print(f'Нельзя скопировать файл {file_name}.')
    else:
        print(f'Файл {file_name} успешно скопирован.')

if __name__ == '__main__':
    while True:
        print("1 - Создать папки dir1-dir9")
        print("2 - Удалить папки dir1-dir9")
        print("3 - Вывести список папок в данной директории")
        print("4 - Скопировать текущий файл")
        print("5 - выйти из программы")
        command = input("Введите номер команды: ")
        if command == '1':
            for i in range(1, 10):
                make_dir(f"dir{i}")
        elif command == '2':
            for i in range(1, 10):
                del_dir(f"dir{i}")
        elif command == '3':
            list_dir()
        elif command == '4':
            copy_file(__file__)
        elif command == '5':
            break
