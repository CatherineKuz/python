# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

import random

class Person:
    def __init__(self, name, surname, group, birth_date, patronus, mother, father):
        self.name = name
        self.surname = surname
        self.group = group
        self.patronus = patronus
        self.birth_date = birth_date

    def full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronus

    def short_name(self):
        return self.surname + ' ' + self.name[0] + '. ' + self.patronus[0] + '.'

class Student(Person):
    def __init__(self, name, surname, patronus, mother, father, group):
        Person.__init__(self, name, surname, patronus, birth_date)
        self.group = {'group_num': int(group.split()[0]), 'group_char': group.split()[1]}
        self.mother = mother
        self.father = father

    def graduate(self):
        self.group['group_num'] += 1

    def get_group(self):
        return str(self.group['group_num'] + ' ' + self.group['group_char'])

    def student_info(self):
        print('Ученик')
        print(f'ФИО: {student.surname} {student.name} {student.patronus}')
        print(f'Дата рождения: {student.birth_date}')
        print(f'Класс: {student.get_group}')
        print(f'Родители: {student.mother} {student.father}')

class Teacher(Person):
    def __init__(self, name, surname, patronus, birth_date, science, teaching_groups):
        Person.__init__(self, name, surname, patronus, birth_date)
        self.science = science
        self.teaching_groups = teaching_groups

    def convert_group(self, group):
        return {'group_num': int(group.split()[0]), 'group_char': group.split(0)[1]}

    def get_groups(self):
        group_lst = []
        for group in self.teaching_groups:
            group_name = str(group['group_num']) + ' ' + group['group_char']
            group_lst.append(group_name)
        return group_lst

    def teacher_info(self):
        print('Учитель')
        print(f'ФИО: {teacher.surname} {teacher,name} {teacher.patronus}')
        print(f'Дата рождения: {teacher.birth_date}')
        print(f'Предмет: {teacher.science}')
        print(f'Ведет классы: {teacher.get_groups}')


male_names = ["Василий", "Александр", "Сергей"]
female_names = ["Ирина", "Анна", "Анастасия"]
male_surnames = ["Несов", "Давыдов", "Иванов"]
female_surnames = ["Свиридова", "Политова", "Лавренева"]
male_patronus = ["Иванович", "Сергеевич", "Александрович"]
female_patronus = ["Владимировна", "Сергеевна", "Игоревна"]
birth_dates = ["14.02.1996", "07.03.2001", "19.11.2001"]
birth_dates_adults = ['04.12.1985', '01.03.1978', '29.04.1979']
sciences = ["Математика", "Физика", "Геометрия"]
initials = ["И.А.", "О.В.", "В.Е."]
groups = ["8 а", "3 б", "5 в"]

students = []
teachers = []

for i in range(20):
    male_student = Student(random.choice(male_names), random.choice(male_surnames), random.choice(birth_dates))
    female_student = Student(random.choice(female_names), random.choice(female_surnames), random.choice(birth_dates))
    students.append(male_student)
    students.append(female_student)

for i in range(3):
    group_list = []
    for j in range(random.randrange(4, 5)):
        group_list.append(random.choice(groups))
        while group_list.count(group_list[j]) > 1:
            group_list[j] = random.choice(groups)

    male_teacher = Teacher(random.choice(male_names), random.choice(male_surnames), random.choice(birth_dates_adults), random.choice(sciences))

    for k in range(len(sciences)):
        try:
            if sciences[k] == male_teacher.science:
                sciences.pop(k)
        except IndexError:
            pass

    group_list = []
    for j in range(random.randrange(4, 5)):
        group_list.append(random.choice(groups))
        while group_list.count(group_list[j]) > 1:
            group_list[j] = random.choice(groups)

    female_teacher = Teacher(random.choice(female_names), random.choice(female_surnames), random.choice(birth_dates_adults), random.choice(sciences))

    for k in range(len(sciences)):
        try:
            if sciences[k] == female_teacher.science:
                sciences.pop(k)
        except IndexError:
            pass

    teachers.append(male_teacher)
    teachers.append(female_teacher)

status = 0

while status != 1:

    print('1 - информация о всех учениках')
    print('2 - информация о всех учителях')
    print('3 - полный список всех классов школы')
    print('4 - список всех учеников в указанном классе')
    print('5 - список всех предметов указанного ученика')
    print('6 - ФИО родителей указанного ученика')
    print('7 - список всех Учителей, преподающих в указанном классе')

    mode = int(input('Введите номер действия: '))

    if mode == 1:
        #информация о всех учениках
        for student in students:
            student.student_info()

    elif mode == 2:
        #информация о всех учителях
        for teacher in teachers:
            teacher.teacher_info()

    elif mode == 3:
        #полный список всех классов школы
        all_groups = []
        for student in students:
            if all_groups.count(student.get_group()) == 0:
                all_groups.append(student.get_group())

        print(f'Полный список классов школы, где есть хотя бы один ученик: {all_groups}')

    elif mode == 4:
        #список всех учеников в указанном классе
        inp_group = input("Введите класс в формате 1 А: ")
        students_in_group = []
        for student in students:
            if student.get_group() == inp_group:
                students_in_group.append(student.surname + ' ' + student.name[0] +'. ' + student.patronus[0] + '.')
        print(students_in_group)

    elif mode == 5:
        #список всех предметов указанного ученика
        std_group = ''
        inp_name = input('Введите полные ФИО ученика: ')
        for student in students:
            if (student.surname + ' ' + student.name + ' ' + student.patronus) == inp_name:
                std_group = student.get_group()
        subjs = []
        for teacher in teachers:
            if std_group in teacher.get_groups():
                subjs.append(teacher.subject)
        print(f'{inp_name} изучает следующие предметы: ')


    elif mode == 7:
        #список всех Учителей, преподающих в указанном классе
        tchrs = []
        inp_group = input('Введите класс в формате 1 А:')
        for teacher in teachers:
            if inp_group in teacher.get_group():
                tchrs.append(str(teacher.surname + ' ' + teacher.name + ' ' + teacher.patronus))
        print(f'В классе {inp_group} преподают следующие учителя: ')

    end = input('Завершить работу? Y/N')
    if end == 'Y':
        status = 1




