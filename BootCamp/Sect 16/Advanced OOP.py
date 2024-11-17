"""
class fan:
    def __init__(self, make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.speed = 0
        self.is_on = False

    def __repr__(self):
        return repr((f"Manufacturer is {self.make}",f"Radius is {self.radius}",f"Color is {self.color}",
                     f"Speed is {self.speed}",f"On or Off {self.is_on}"))

    def switch_on(self):
        self.is_on = True
        self.speed = 3
        return print(f"Fan is on {self.is_on}, and speed is {self.speed}")
    def switch_off(self):
        self.is_on = False
        self.speed = 0
        return print(f"Fan is off {self.is_on}, and speed is {self.speed}")
    def increase_speed(self):
        if self.is_on is True:
            self.speed += 1
        return print(f"Speed is increased, {self.speed}")
    def decrease_speed(self):
        if self.is_on is True:
            self.speed -= 1
        return print(f"Speed is decreased, {self.speed}")

kitchen_fan = fan("Honda", "15.5", "Grey")
print(kitchen_fan)
kitchen_fan.switch_on()
kitchen_fan.switch_off()
kitchen_fan.increase_speed()
kitchen_fan.decrease_speed()
kitchen_fan.switch_off()
"""
"""
class Book(object):
    def __init__(self, id, name, author):
        super().__init__()
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []
    def __repr__(self):
        return repr((f"Book id is {self.id}",f"Name of the Book {self.name}",
                     f"Author of the book {self.author}", f"Reviews {self.reviews}"))
    def add_review(self, review):
        self.reviews.append(review)
        setattr(Book, 'add_review', review)

class Review:
    def __init__(self, id, description, rating):
        self.id = id
        self.description = description
        self.rating = rating
    def __repr__(self):
        return repr((f"id {self.id}", f"Description {self.description}",
                    f"Rating {self.rating}"))

book1 = Book(1, "Science", "John")
review = Review(1, "Excellent Books", 5)
book1.add_review(Review(1, "Excellent Book", 5))
print(book1)
"""
"""
class Animal:
    def Bark(self):
        print("Bark")

class Pet(Animal):
    def groom(self):
        print("Groom")

animal1 = Animal()
animal1.Bark()

pet1 = Pet()
pet1.Bark()
pet1.groom()
"""
"""
class Book:
    pass
    def __repr__(self):
        return repr(('New Book'))

book = Book()
print(book)
"""
"""
class LandAnimal:
    def walking_speed(self):
        self.walking_speed = 5
        return self.walking_speed

    def increase_walking_speed(self, How_much):
        self.How_much = How_much
        How_much = self.walking_speed + self.How_much
        return self.How_much

class WaterAnimal:
    def swimming_speed(self):
        self.swimming_speed = 5
        return self.swimming_speed

    def increase_swimming_speed(self, How_much_swimming):
        self.increase_s = How_much_swimming
        self.increase_s = self.increase_s + How_much_swimming
        return self.increase_s

class Amphibians(LandAnimal, WaterAnimal):
    pass

toad = Amphibians()
#print(toad.walking_speed())
print(toad.increase_walking_speed(0))
print(toad.increase_swimming_speed(0))
"""
"""
class LandAnimals:
    def __init__(self):
        super().__init__()
        self.walking_Speed = 5
        print("Walking speed is ",self.walking_Speed)

    def walking_S(self, How_much):
        self.How_much = How_much
        temp = self.How_much + self.walking_Speed
        print("Walking increased by ", temp)

class WaterAnimals:
    def __init__(self):
        super().__init__()
        self.swimming = 5
        print("Swimming speed is ", self.swimming)

    def swimming_S(self, How):
        self.How = How
        temp = self.How + self.swimming
        print("Swimming increased by ", temp)

class Amphibian(LandAnimals, WaterAnimals):
    pass

toad = Amphibian()
toad.walking_S(1)
toad.swimming_S(1)
print(toad)
"""
"""
class Engine:
    def start_engine(self):
        return "Engine started"

class Wheels:
    def number_of_wheels(self):
        no_of_wheel = 4
        return no_of_wheel

class Car(Engine, Wheels):
    def drive(self):
        return "Car is driving"

vehicle = Car()
print(vehicle.drive())

result_start = vehicle.start_engine()
print(result_start)

no_of_wheels = vehicle.number_of_wheels()
print(no_of_wheels)
"""
"""
from abc import abstractmethod, ABC
class abstract_Animal(ABC):
    @abstractmethod
    def bark1(self):
        pass

class Dog(abstract_Animal):
    def bark1(self):
        print("Woof Woof")

Dog2 = Dog()
Dog2.bark1()
"""
"""
from abc import abstractmethod, ABC
class AbstractRecipe(ABC):
    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()
    @abstractmethod
    def prepare(self):
        pass
    @abstractmethod
    def recipe(self):
        pass
    @abstractmethod
    def cleanup(self):
        pass

class Biryani(AbstractRecipe):
    def prepare(self):
        print("Cut Vegetables")
    def recipe(self):
        print("Mix Spices")
    def cleanup(self):
        print("Dishwasher unload")

Bombay_Biryani = Biryani()
Bombay_Biryani.execute()
"""
"""
class shape:
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        self.area = 3.141 * self.radius * self.radius
        return print("Area of a Circle is ",self.area)

class square(shape):
    def __init__(self, area1):
        self.area1 = area1
    def area(self):
        self.area = self.area1 * self.area1
        return print("Area of a Square is ", self.area)

class rectangle(shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        self.area = self.width * self.length
        return print("Area of a rectangle is ", self.area)

circle1 = circle(3)
circle1.area()

square1 = square(4)
square1.area()

rectangle1 = rectangle(2, 3)
rectangle1.area()

shapes = [circle(3), square(4), rectangle(2, 3)]
for shape in shapes:
    print(shape.area())
"""
"""
from abc import ABC, abstractmethod
class shape(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        areas = self.length * self.width
        return areas
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

class Circle(shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        areas = 3.14 * (self.radius ** 2)
        return areas
    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter

shape1 = Rectangle(2, 3)
print(shape1.area())
print(shape1.perimeter())


shape2 = Circle(2)
print(shape2.area())
print(shape2.perimeter())
"""