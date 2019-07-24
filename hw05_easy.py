# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

path_dir = [('dir_' + str(i + 1)) for i in range(9)]

def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print(dir_path + ' - такая директория уже есть')

def del_dir(paths):
    try:
        os.rmdir(paths)
    except:
        print("Удалить директорию %s не удалось" % paths)
    else:
        print("Успешно удалена директория %s" % paths)

for i in path_dir:
    make_dir(i)
    del_dir(i)



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def list_dir ():
    folders = os.listdir()
    print('Список папок:')
    for index, element in enumerate(folders, start=1):
        if os.path.isdir(element):
            print('{}. {}'.format(index, element))

if __name__ == '__main__':
    list_dir()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def current_file_copy ():
    name_file = os.path.relpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Копия файла уже существует'

if __name__ == '__main__':
    print(current_file_copy())
