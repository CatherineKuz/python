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


