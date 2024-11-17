"""
class Customer:
    def _init_(self, name, address):
    self.name = name
    self.address = address
"""
from pkg_resources import distributions_from_metadata

"""
class Country:
pakistan = Country()
pakistan.capital = 'Islamabad'
print(pakistan.capital)
"""
"""
class Motorbike:
    pass
Honda_Motor = Motorbike()
Duccati = Motorbike()

Honda_Motor.name = 'The Art of Computer Programming'
Duccati.speed = 250

print(Honda_Motor.name)
print(Duccati.speed)
"""
"""
class Book:
    pass
first_book = Book()
secound_book = Book()
third_book = Book()
first_book.name = "The Stationary shop in Tehran"
secound_book.name = "The Kite Runner"
third_book.name = "A Thousand Splendid Suns"

print(first_book.name)
"""
"""
class Planet:
    pass
earth = Planet()
earth.name = 'Earth'
venus = Planet()
venus.name = 'Venus'
print(earth.name)
print(venus.name)

venus.do_something()
"""
"""
class Country:
    pass
india = Country()
Pakistan = Country()

india.name = 'India'
Pakistan.name = 'Pakistan'

print(india.name)
print(Pakistan.name)
"""
"""
class MotorBike:
    pass
Honda = MotorBike()
Duccati = MotorBike()

Honda.speed = 50
Duccati.speed = 120

print(Honda.speed)
print(Duccati.speed)
"""
"""
class Book:
    pass
firstbook = Book()
firstbook.name = 'The Kite Runner'
print(firstbook.name)
"""
"""
class planet:
    pass
earth = planet()
venus  = planet()

earth.name = 'The OG Earth'
venus.name = 'Brightest Planet in the sky'

print(earth.name)
print(venus.name)
"""
"""
class Motorbike:
    def __init__(self, speed):
        #print("Instance is created")
        self.speed = speed
        #print(f"This is {speed}")
honda = Motorbike(450)
Ducaati = Motorbike(110)
print(honda.speed)
"""
"""
class Book:
    def __init__(self):
        self.name = self

First_Book = Book()
First_Book.name = "The Kite Runner"
print(First_Book.name)
"""
"""
class planet:
    def __init__(self):
        print("Instance is created")
    def __init__(self, name):
        self.name = name
        print("New Instance is created")
        print(self.name)
venus = planet("The Venus")
"""
"""
class planet():
    def __init__(self, name='Earth'):
        print("Best Constructor Practice")
        self.name = name
        self.speed = 10
        self.dis_from_sun = 100
planet = planet()
print(planet.dis_from_sun)
"""
"""
class Dimension:
    def __init__(self, inches, feet):
        self.inches = inches
        self.feet = inches / 12
        if self.inches < 0:
            self.inches = -1
            self.feet = -1
        else:
            self.inches = inches
Dimension1 = Dimension(24, 24)
print(Dimension1.inches)
print(Dimension1.feet)
"""
"""
class Dimension:
    def __init__(self, inches):
        self.inches = inches
        if self.inches >= 0:
            self.feet =int(inches/12)
            self.inches = inches%12
        else:
            self.inches = -1
            self.feet = -1
dm = Dimension(25)
print(dm.feet)
print(dm.inches)
"""
"""
class car:
    pass
my_Car = car()
print(type(my_Car))
"""
"""
class myclass:
     def class_method(self):
         pass
class1 = myclass()
class1.class_method()
"""
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.width * self.length
area1 = Rectangle(5, 3)
print(area1.area())
"""
"""
class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Current amount", self.balance)

    def deposits(self, amount):
        self.balance += amount
        print("Deposit amount", self.balance)

    def withdrawl(self, amount):
        self.balance -= amount
        print("Withdrawl amount", self.balance)

    def get_balance(self):
        return self.balance
account1 = BankAccount()
account1.deposits(2000)
account1.withdrawl(500)
account1.get_balance()
print(account1.get_balance())
"""
class RGBColor:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    def invert(self):
        self.red = 255 - self.red
        print("Red", self.red)

        self.green = 255 - self.green
        print("Green", self.green)

        self.blue = 255 - self.blue
        print("Blue", self.blue)

color = RGBColor(25,105, 55)
color.invert()

