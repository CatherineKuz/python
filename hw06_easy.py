# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt

class Triangle:
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        self.AB = sqrt((Bx - Ax) ** 2 + (By - Ay) ** 2)
        self.BC = sqrt((Cx - Bx) ** 2 + (Cy - By) ** 2)
        self.AC = sqrt((Cx - Ax) ** 2 + (Cy - Ay) ** 2)

    def perimeter(self):
        return self.AB + self.BC + self.AC

    def square(self): # для расчетов я использовала формулу Герона
        p = self.perimeter / 2
        return sqrt(p * (p - self.AB) * (p - self.BC) * (p - self.AC))

    def heighttoab(self):
        return 2 * self.square / self.AB
        #высоты к другим сторонам рассчитываются аналогично


triangle1 = Triangle(2, 3, 3, 5, 6, 3)

print(triangle1.perimeter())
print(triangle1.square())
print(triangle1.heighttoab())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
        self.AB = sqrt((Bx - Ax) ** 2 + (By - Ay) ** 2)
        self.BC = sqrt((Cx - Bx) ** 2 + (Cy - By) ** 2)
        self.CD = sqrt((Dx - Cx) ** 2 + (Dy - Cy) ** 2)
        self.AD = sqrt((Dx - Ax) ** 2 + (Dy - Ay) ** 2)
        self.AC = sqrt((Cx - Ax) ** 2 + (Cy - Ay) ** 2) #диагональ 1
        self.BD = sqrt((Dx - Bx) ** 2 + (Dy - By) ** 2) #диагональ 2

    def trap_check(self):
        if self.AC == self.BD:
            return print("Это равнобедренная трапеция")
        else:
            return print("Это не равнобедренная трапеция")

    def perimeter(self):
        return self.AB + self.BC + self.CD + self.AD


trapezoid1 = Trapezoid(0, 0, 1, 2, 3, 2, 4, 0)
print(trapezoid1.trap_check())
print("Сторона АВ равна " + str(trapezoid1.AB)) #то же самое для остальных сторон
print("Периметр равен " + str(trapezoid1.perimeter()))