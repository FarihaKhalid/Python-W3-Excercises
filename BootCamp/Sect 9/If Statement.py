"""i = 5
#if i > 3:
    #print(f"{i} is greater than 3")
if True:
    print("This is true")
if False:
    print("This is False")"""
from PIL.ImImagePlugin import number
from gi.types import nothing

"""
a = 5
b = 6

if (a > b):
    print(f"{a} is greater than {b}")
if (b > a):
    print(f"{b}(b) is greater than {a}(a)")"""
"""
def is_valid_triangle(angle1, angle2, angle3):
    valid_triangle = angle1 + angle2 + angle3
    if valid_triangle == 180:
        return True
    else:
        return False

result = is_valid_triangle(50, 60,  90)
print(result)"""

"""
def calculate_sum_of_divisors(number):
    sum = 0
    for i in range(1, number + 1 , 1):
        if number % i == 0:
            sum = sum + i
            #print("this is stupid ", sum)
        else:
            pass
    return sum
result = calculate_sum_of_divisors(15)
print(result)"""

"""
def is_perfect_number(number):
    if number >= 1:
        sum = 0
        for i in range(1, number, 1):
            if number % i == 0:
                sum = sum + i
                #print("This is sum", sum)
            else:
                pass
        if sum == number:
            return True
        else:
            return False
    elif number <= 0:
        return False

result = is_perfect_number(-1)
print(result)
"""
"""
def get_last_digit(number):
    last_digit = number % 10
    return last_digit
result = get_last_digit(6)
print(result)"""

"""
i = 3
if i%2 == 0:
    print("i is even")
else:
    print("i is odd")
"""
"""
i = 4
if i>0:
    print("i is 1")
elif i==4:
    print("i is 2")
else:
    print("i is not 1 or 2")
"""
"""
if (False):
    print("False")
"""
"""
x = -6
if x:
    print("Something")
"""
"""
k = 15
if (k > 20):
    print(1)
elif (k > 10):
    print(2)
elif (k < 20):
    print(3)
else:
    print(4)
"""
"""
i = 15
if (i < 20):
    print("i < 20")
elif (i > 20):
    print("i > 20")
else:
    print("who am I")
"""
"""
a = 2
b = 20
if a > 5:
    if b < 30:
        print("Inner condition met")
    else:
        print("Inner condition do not met")
else:
    print("Outer condition not met")
"""
"""
m = 15
if m > 20:
    if m < 20:
        print("m > 20")
    else:
        print("who am I")
"""
"""
number = 5
if number > 0:
    number = number + 10
    #print(number)
number = number + 5
print(number)
"""
"""
number = 4
if number%2 == 0:
    isEven = True
else:
    isEven = False
print(isEven)
"""
"""
x = 10
y = 5
if x > 5 and y < 10:
    print("Condition 1")
elif x == 10 and y == 5:
    print("Condition 2")
else:
    print("Condition 3")
"""
"""
x = 5
if not x == 3:
    print("x is not equal 3")
else:
    print("x is equal to 3")
"""
"""
number = 5
#isEven = True
if number % 2 == 0:
    isEven = True
else:
    isEven = False
print(isEven)
"""
"""
def assign_grade(marks):
    grade = ""
    if marks >= 90:
        grade = 'A'
        print(grade)
    elif marks <= 89 and marks >= 80:
        grade = 'B'
        print(grade)
    elif marks <= 79 and marks >= 70:
        grade = 'C'
        print(grade)
    elif marks <= 69 and marks >= 60:
        grade = 'D'
        print(grade)
    elif marks < 60 and marks >= 50:
        grade = 'E'
        print(grade)
    else:
        grade = 'F'
        print(grade)
    return grade
res = assign_grade(90)"""
"""

def provide_weather_advisory(temprature):
    advisory = ""
    if temprature < 0:
        advisory = "It's freezing! Wear a heavy coat."
        print(advisory)
    elif temprature <= 10 or temprature == 0:
        advisory = "It's cold! Bundle up."
        print(advisory)
    elif temprature >= 11 and temprature <= 20:
        advisory = "It's cool! A light jacket will do."
        print(advisory)
    elif temprature > 20:
        advisory = "It's warm! Enjoy the day."
        print(advisory)
    return advisory
(provide_weather_advisory(10))"""