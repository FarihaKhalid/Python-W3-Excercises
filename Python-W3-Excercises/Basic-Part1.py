"""
#QNO1
print("Twinkle, twinkle, little star,\n""\t How I wonder what you are!\n""\t\t Up above the world so high,\n"
      "\t\tLike a diamond in the sky.""\nTwinkle, twinkle, little star,\n""\tHow I wonder what you are")
"""
from sndhdr import tests

"""
#QNO2
import sys
print(sys.version)
"""
"""
#QNO3
time = datetime.now()
print(time)
"""
"""
#QNO4
radius = float(input("r = "))
area = (radius * radius) * float(3.141)
print(area)
"""
"""
#QNO5
first_name = input("First name: ")
last_name = input("Last name: ")
first_last_name = first_name + " " + last_name
x = len(first_last_name) -1
print(first_last_name)

for i in range(len(first_last_name)):
      print(first_last_name[x])
      x = x - 1
"""
"""
#QNO6
data = input("Sample Data: ")
data_list = data.split(",")
my_tuple = tuple(data_list)
print(data_list)
print(my_tuple)
"""
"""
#QNO7
file_name = input("Sample filename: ")
extension = file_name.split(".")
print("Output:", extension[-1])
"""
"""
#QNO8
color_list = ["Red","Green","White" ,"Black"]
print("First Color: ",color_list[0],"\n","Second Color: ", color_list[-1])
"""
"""
#QNO9
date = 11, 12, 2014
print(f"exam_st_date = {(11, 12, 2014)}")
print(f"Sample Output : The examination will start from : %i / %i / %i" %date)
"""
"""
#QNO10
str_num = input("Sample value of n is ", )
str_num_a = str_num + str_num
str_num_aa = str_num_a + str_num
result = int(str_num) + int(str_num_a) + int(str_num_aa)
print("Expected Result : ", result)
"""
"""
#QNO11
function = input("Sample function : ")
print("Expected Result : ", function.__doc__)
"""
"""
#QNO12
month1 = input("Month ")
year1 = input("Year ")
print(month(int(year1),int(month1)))
"""
"""
#QNO13
print("a string that you ""'don't"" have to escape\nThis \nis a ....... multi-line \n"
      "heredoc string --------> example")
"""
"""
#QNO14
f_date = date(2014, 7, 11)
l_date = date(2014, 7, 2)
diff = f_date - l_date
print(diff.days, "days")
"""
"""
#QNO15
volume = float(4/3) * 3.141
radius = 6 * 6 * 6
result = volume * radius
print("Volume", result)
"""
"""
#QNO16
num = input("Number: ")
num = int(num)
absolute_difference = 0
if num > 17:
      absolute_difference = (num - 17) * 2
else:
      absolute_difference = 17 - num

print(absolute_difference)
"""
"""
#QNO17
number = input("Number: ")
number = int(number)
if number > 0 and number <= 100:
      print("In range of 100")
elif 101 <= number <= 1000:
      print("In range of 1000")
else:
      print("In range of 2000")
"""
"""
#QNO18
number1 = int(input("Number 01: "))
number2 = int(input("Number 02: "))
number3 = int(input("Number 03: "))
result = 0
if number1 == number2 == number3:
      result = (number1 + number2 + number1) * 3
else:
      result = number1 + number2 + number3
print(result)
"""
"""
#QNO19
string = input("This has been added: ")
string1 = string.split()

if string1[0] != 'Is':
      print('Is ' + string)
else:
      print(string)
"""
"""
#QNO20
def larger_string(text, n):
      result = ''
      for i in range(n):
            result = result + text
      return result
print(larger_string(".test", 3))
"""
"""
#QNO21
def even_odd(number):
      number = int(number)
      if number % 2 == 0:
            print(f"{number} is even")
      else:
            print(f"{number} is odd")
result = even_odd(input("Number: "))
"""
"""
#QNO22'
input1 = input("List here: ")
list1 = []
for i in input1:
    i = int(i)
    list1.append(i)
count = list1.count(4)
print(count)
"""
"""
#QNO23
def copies_of_string():
    string = input("String here: ")
    n_no_of_copies = int(input("Number of Copies: "))
    result = ''
    string1 = ''
    for s in range(2):
        string1 = string1 + string[s]
    if n_no_of_copies >= 2:
        for i in range(n_no_of_copies):
            result = result + string1
    else:
        result = string
    return result
result = copies_of_string()
print(result)
"""
"""
#QNO24
def vowel_or_not():
    list_of_vowels = ['a','e','i','o','u']
    search1 = input("Character input: ")
    if search1 in list_of_vowels:
        print(f"This is {search1} vowel")
    else:
        print(f"This is not {search1} vowel")

result = vowel_or_not()
print(result)
"""
"""
#QNO25
def found_or_not():
    search = int(input("Number to search: "))
    group_Value =  [1, 5, 8, 3]
    if search in group_Value:
        return True
    else:
        return False
result = found_or_not()
print(result)
"""
"""
#QNO26
def histogram(items):
    for i in items:
        design = ''
        for s in range(i):
            design = design + '@'
        print(design)

histogram([2,3,6,5])
"""
"""
#QNO27
def concat_String(lists):
    concat_string = ''
    for i in lists:
        concat_string = concat_string + str(i)
    return concat_string
result = concat_String([1,5,12,2])
print(result)
"""
"""
#QNO28
def even_in_list(lists):
    even_list = []
    for i in lists:
        if i % 2 == 0 and i < 237:
            even_list.append(i)
        else:
            continue
    return even_list

result = even_in_list([
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ])
print(result)
"""
#QNO29
"""
color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]
list = [x for x in color_list_1 if x not in color_list_2]
print(list)
color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]
#difference1 = (set(color_list_1)).difference(set(color_list_2))
difference1 = set(color_list_2)^set(color_list_1)
print(difference1)
"""
"""
#QNO30
def area_of_triangle(base, height):
    area = 0.5 * ((base) * (height))
    return area
result = area_of_triangle(20, 40)
print(result)
"""
"""
#QNO31
num = int(input("NO 1: "))
num1 = int(input("NO 2: "))
res = min(num,num1)
GCD = 0
i = num
for i in range(num, 0, -1):
    if (num % i == 0) and (num1 % i == 0):
        print(i)
        break
    else:
        continue
"""
"""
#QNO32
num = int(input("NO 1: "))
num1 = int(input("NO 2: "))
factor_num = []
factor_num1 = []
common_factor = []
LCM = 0
HCF = 1
#Factors of num
for i in range(2,num+1,1):
    if num%i == 0:
        factor_num.append(i)

for i in range(2,num1+1,1):
    if num1%i == 0:
        factor_num1.append(i)
common_factor = list(set(factor_num).intersection(factor_num1))
if len(common_factor) == 0:
    LCM = (num * num1)
else:
    HCF = max(common_factor)
    LCM = (num * num1)/HCF

print(LCM)
"""
"""
#QNO 33
def sum_of_numbers(n1, n2, n3):
    if n1 == n2 or n2 == n3 or n3 == n1:
        sum1 = 0
    else:
        sum1 = n1 + n2 + n3
    return sum1

result = sum_of_numbers(1,1,2)
print(result)
"""
"""
#QNO34
def sum_of_integers(n1, n2):
    sum1 = n1 + n2
    if sum1 in range(15, 21):
        sum1 = 20
    return sum1
result = sum_of_integers(10, 12)
print(result)
"""
"""
#QNO35
def complicated(n1, n2):
    ans = True
    sum1 = n1 + n2
    diff = n1 - n2
    if n1 == n2 or sum1 == 5 or diff == 5:
        ans = True
    else:
        ans = False
    return ans
result = complicated(7, 3)
print(result)
"""
"""
#QNO36
def add_if_odd(n1, n2):
    sum1 = 0
    if type(n1) == int and type(n2) == int:
        sum1 = n1 + n2
        return sum1
    else:
        return print("Input must be in integers ")
result = add_if_odd('5',20.23)
print(result)
"""
"""
#QNO37
print("Fariha Khalid \n610 Spur Ridge \n31")
"""
"""
#QNO38
def solution(n1, n2):
    test_date = (n1 + n2) * (n1 + n2)
    return test_date
result = solution(4, 3)
print(result)
"""
"""
#QNO39
def future_investment(amt, int_rate, years):
    future_rate = amt * ((1 + (0.01 * int_rate)) ** years)
    return future_rate
result = future_investment(10000, 3.5, 7)
print(result)
"""
"""
#QNO40
import math
list1 = [4, 0]
list2 = [6, 6]
distance = math.sqrt((list1[0] - list2[0]) ** 2 + (list1[1] - list2[1]) ** 2)
print(distance)
"""

