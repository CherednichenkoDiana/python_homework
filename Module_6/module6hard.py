import math

class Figure:
    sides_count = 0
    def __init__(self, __color, *__sides):
        self.filled = True
        self.__color = __color

        self.__sides = []
        if len(__sides) == self.sides_count:
            for side in __sides:
                self.__sides.append(side)
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        if (r >= 0 and r <= 255) & (g >= 0 and g <= 255) & (b >= 0 and b <= 255):
            return True
        else:
            return False

    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color = r,g,b

    def __is_valid_sides(self,*sides):
        if len(sides) != len(self.__sides):
            return False
        else:
            for side in sides:
                if isinstance(side,int) & (side > 0):
                    continue
                else:
                    return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimeter = 0
        for side in self.__sides:
            perimeter += side
        return perimeter

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            sides_new = []
            for side in new_sides:
                sides_new.append(side)
            self.__sides = sides_new

class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
        self.__radius = self.__len__()

    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)

    def get_square(self):
        sides = self.get_sides()
        a = sides[0]
        b = sides[1]
        c = sides[2]
        p = self.__len__() / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)
        sides = []
        for i in range(self.sides_count):
            sides.append(__sides[0])
        self.set_sides(*sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3

if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    triangle1 = Triangle((0,0,0),6,8,10)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка площадь (треугольника):
    print(triangle1.get_square())

    # Проверка объёма (куба):
    print(cube1.get_volume())
