"""
def is_prime(number):
    prime = True
    if number >= 2:
        for i in range(2, number):
            if number%i == 0:
                prime = False
    else:
        prime = False
    return prime

res = is_prime(2)
print(res)
"""
from orca.punctuation_settings import cube_root

"""
i = -2
while i < 5:
    print(i)
    i = i + 1
"""
"""
def sum_of_squares_upto_limit(number):
    i = 0
    sum = 0
    while sum <= number:
        i = i + 1
        sum = sum + (i * i)
        #print(sum)
    return sum
res = sum_of_squares_upto_limit(30)
"""
"""
def sum_of_cubes_upto_limit(number):
    i = 0
    sum = 0
    while sum < number:
        cube = i * i * i
        sum = sum + cube
        i = i + 1
    return sum
res = sum_of_cubes_upto_limit(100)
print(res)
"""
"""
def get_number_of_digits(number):
    total = 0
    if number > 0:
        while number > 0:
            number = number // 10
            total = total + 1
    elif number == 0:
        total = 1
    else:
        total = -1
    return total
res = get_number_of_digits(0)
print(res)
"""
