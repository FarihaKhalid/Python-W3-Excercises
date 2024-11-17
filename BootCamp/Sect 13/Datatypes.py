"""print(type(2.5))
print(type(2))"""
from email.contentmanager import raw_data_manager

from jinja2.nodes import Break

"""
print((type(5)))
print(type(2/5))
"""
"""
def calculate_simple_function(principal, interest, duration):
    total = principal + (principal * interest * 0.01 * duration)
    return total
total = calculate_simple_function(10000, 5, 5)
print(total)"""
"""
i = 1
i = i + 1
print(i)

i += 1
print(i)

i -= 1
print(i)

i *= 2
print(i)
i /= 2
print(i)
i = ++i
print(i)
"""
"""
no1 = 5
no2 = 2
print(no1//no2)

no1 //= no2
print(no1)
"""
"""
print(5 ** 3)
print(pow(5,3))
"""
"""
print(int(5.9258))
print(round(5.9258))
print(float(3))
"""

"""
from decimal import Decimal
value1 = Decimal('4.9')
value2 = Decimal('3.9')
result = value1 - value2
print(result)
"""

"""
import math
print(math.pi)
print(math.e)"""

"""
i = 10
print(i > 15)
print(i >= 15)
print(i == 15)
print(i <= 15)
print(i < 15)
"""

"""
x = 3.5
y = 4
z = True

print(type(x))
print(type(y))
print(type(z))
"""
"""
a = 5
b = 2.5
res = a + b
print(res)
"""
"""
c = True
b = False
res = c + b
print(res)
"""
"""
num = 7
num1 = float(num)
print(num1)
"""
"""
num_float = 3.18
num_int = int(num_float)
print(num_int)
"""

"""
is_raining = True
int_value = int(is_raining)
print(int_value)
"""
"""
str_num = 123
int_num = int(str_num)
print(int_num)
"""
"""
str_num = "3.12"
num = float(str_num)
print(num)
"""
"""
num = 10
str_num = str(num)
print(str_num)
print(type(str_num))
"""

"""
is_True= True
str_bool = str(is_True)
print(str_bool)"""

"""
def is_eligible_for_race(max_speed):
    return max_speed == 200

res = is_eligible_for_race(200)
res1 = is_eligible_for_race(320)
print(res)
print(res1)"""
"""
print(type(5))
"""
"""
marks = [22, 23, 24]
marks.append(25)

print(len(marks))
print(sum(marks)/len(marks))
print(marks)
print(max(marks))
print(min(marks))
print(marks[1])

marks.insert(2, 444)
print(marks)

marks.append(333)
print(marks)

marks.remove(333)
print(marks)

print(marks.reverse())

print(444 in marks)
print(666 in marks)

print(marks.count(2))

print(marks.index(444))

for mark in marks:
    print(mark)
"""
"""
def has_greater_element(numbers, value):
    check = False
    for number in numbers:
        if number > value:
            check = True
            break
    return check
no = []
print(has_greater_element(no, 10))
"""
"""
animals = ['Cat', 'Dog', 'Crow']
print(animals)
#print(len(animals))
#print(animals[0])
#del (animals[1])
#x`print(animals)
#print(animals[9])

animals.extend(["Bird"])
animals.append(10)
del animals[4]

print(animals[-3])
"""
"""
mixed_list = ['4','1','2']
mixed_list.sort()
print(type(mixed_list))
mixed_list.append(6)
print(mixed_list)
"""
"""
numbers = [4, 2, 9, 1]
numbers.sort()
#numbers.reverse()
print(numbers)"""
"""
def are_sums_equal(list1, list2):
    sum1 = 0
    sum2 = 0
    ans = False
    if len(list1) > 0 and len(list2) > 0:
        for i in list1:
            sum1 += i
        for j in list2:
            sum2 += j
        if sum1 == sum2:
            ans = True
        else:
            ans = False
    else:
        ans = False
    return ans
mes = are_sums_equal([1, 2, 3, 4], [4, 3, 2, 1])
print(mes)
"""
"""
numbers = [1, 2, 3, 4]
#numbers.reverse()
for number in reversed(numbers):
    print(number)
print(numbers)"""
"""
numbers = [7, 2, 3, 4]
numbers.sort()
for number in sorted(numbers):
    print(number)
print(numbers)"""
"""
numbers = ["One", "Two", "Three", "Seven"]
for number in sorted(numbers, key=len, reverse=True):
    print(number)
"""
"""
def is_list_sorted(list1):
    total_no = len(list1)
    next_no = 1
    while total_no > 0:
        total_no -= -1
        for no1 in list1:
            if no1 < list1[next_no]:
                next_no = no1 + next_no
                print("no1", no1)
                print("Next number",total_no)
                print(True)
            else:
                print(False)
res = is_list_sorted([1, 2, 66])
"""
"""
def is_list_sorted(lists):
    ii = 0
    no = 1
    end = 1
    ans = ''
    empty = len(lists)
    if empty > 1:
        for i in lists:
            end += 1
            if end <= len(lists):
                ii  += 1
                no = lists[ii]
                if i <= no:
                    ans = True
                else:
                    ans = False
                    break
    else:
        ans =  True
    return ans
result = is_list_sorted([''])
print(result)
"""
"""
def reverse_list(list0):
    start = 0
    end = len(list0)
    rev_list= []
    for i in list0:
        end = end - 1
        append_item = list0[end]
        rev_list.append(append_item)
        #print(rev_list)
    return rev_list
result = reverse_list([''])
print(result)
"""
"""
def find_factors(number):
    end = number
    factor = []
    while end > 0:
        end -= 1
        for i in range(1, number+1):
            end -= 1
            if number % i == 0:
                factor.append(i)
            else:
                continue
    return factor
result = find_factors(12)
print(result)
"""
"""
def find_multiples(number1, number2):
    multiple1 = 0
    multiple_List = []
    for i in range(1, number2):
        multiple1 = number1 * i
        if multiple1 < number2:
            multiple_List.append(multiple1)
        else:
            break
    return multiple_List
result = find_multiples(5, 26)
print(result)
"""
"""
list1 = [30, 70]
#print(70 in list1)
print(list1)
print(list1)
"""


