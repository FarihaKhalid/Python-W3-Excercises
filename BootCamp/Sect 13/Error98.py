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
        x1 = self.x
        y1 = self.y

        x2 = other
        y2 = other
        d = math.sqrt((x2 - x1) ** 2 + ((y2 - y1) ** 2))
        print(d)

point1 = Point(3, 4)
point1.move(1, 2)
point1.distance_to(7)