"""
class Motorbike:
    def __init__(self, speed):
        self.speed = speed
    def increase_speed(self, how_much):
        self.speed += how_much
    def decrese_speed(self, how_much):
        self.speed -= how_much
Honda = Motorbike(50)
Ducati = Motorbike(80)

Honda.increase_speed(100)
Honda.decrese_speed(20)

Ducati.increase_speed(10)
Ducati.decrese_speed(20)

print(Honda.speed)
print(Ducati.speed)
"""
"""
class Copies:
    def __init__(self, copies, name):
        self.name = name
        self.copies = copies

    def increase_amount(self, increase_copies):
        self.copies += increase_copies

    def decrese_amount(self, decrease_copies):
        self.copies -= decrease_copies

Book1 = Copies(2, "The Kite Runner")
Book1.increase_amount(2)
Book1.decrese_amount(1)

print(Book1.copies, Book1.name)
"""
"""
class planet:
    def rotate(self):
        print("rotate")
    def revole(self):
        print("revolve")
    def rotate_revolve(self):
        self.rotate()
        self.revole()
        #print(self.rotate(), self.revole())
earth = planet()
earth.rotate_revolve()
"""
"""
class Square:
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        if self.side > 0:
            a = self.side * self.side
            print(a)
        else:
            a = -1
            print(a)
    def calculate_perimeter(self):
        if self.side > 0:
            parameter = 0
            parameter = self.side * 4
            print(parameter)
        else:
            a = -1
            print(a)

square1 = Square(-2)
square1.calculate_area()
square1.calculate_perimeter()
"""
"""
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x  = self.x + dx
        self.y = self.y + dy
        print(self.x, self.y)

    def distance_to(self, other):
        x1 = other
        y1 = other
        d = math.sqrt((x1 - self.x) ** 2 + ((y1 - self.y) ** 2))
        print(d)

point1 = Point(3, 4)
point1.move(1, 2)
point1.distance_to(6)
"""
"""
class Motorbike:
    def __init__(self, speed):
        self.speed = speed
    def increase_speed(self, inc):
        self.inc = inc
        self.speed += inc
        print(self.speed)
    def decrease_speed(self, dec):
        if self.speed - dec >= 0:
            self.speed -= dec
            print(self.speed)
        else:
            print("Invalid operation")
Honda = Motorbike(10)
Honda.increase_speed(0)
Honda.decrease_speed(30)
"""
"""
print(type("s"))
print(type(5.5))
print(type(4))
print(type(True))
"""
def something():
    print("This is print")
test = something
test()