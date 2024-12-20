"""
#QNO1
def distinguishing(list1):
    length = len(list1) -1
    for i in range(length):
        s = i + 1
        for k in range(s, length):
            ii = list1[i]
            kk = list1[k]
            if ii == kk:
                return True
                break
    return False

result = distinguishing([5, 4, 5, 7, 9])
print(result)
"""

"""
#QNO2
string = ['a','e','i','o','u']
random.shuffle(string)
print(''.join(string))
"""
"""
#QNO3
list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
last = len(list)
k = 2
i = len(list)
while i > 0:
    i = i - 1
    k = 2
    if k < len(list):
        print(list.pop(k))
        k = k + 2
    else:
        print(list.pop(-1))
"""
"""
#QNO4
list = [1, -6, 4, 2, -1, 2, 0, -2, 0]
three_Sum_list = []
for i in range(len(list)):
    for k in range(i+1,len(list)):
        j = k + 1
        if j in range(2,len(list)-4):
            j = k + 1
            sum1 = list[i] + list[k] + list[j]
            if sum1 == 0:
                three_Sum_list.append(list[i])
                three_Sum_list.append(list[k])
                three_Sum_list.append(list[j])
                break
            else:
                continue
print(three_Sum_list)
"""
"""
#QNO5
numbers = []
for no in range(20):
    d = str(no).zfill(2)

numbers.append(d)
print(numbers)
"""
"""
#QNO6
string_input = input("String: ")
text = string_input.split()
counter_text = []
string_List = []
value = ""
for s in text:
    counter_text = text.count(s)
    test1 = s
    if test1 not in string_List:
        string_List.append(test1)
        string_List.append(counter_text)
    else:
        continue
print(string_List)
"""
"""
#QNO7
file = open("file1.txt", "r")
content = file.read()
counter = 0
char_counter = []

for chr in content:
    counter = content.count(chr)
    if chr not in char_counter:
        char_counter.append(chr)
        char_counter.append(counter)
    else:
        continue
for u in char_counter:
print(char_counter)
"""
"""
#QNO08
URL = "https://news.google.com/home?hl=en-US&gl=US&ceid=US:en"
response = requests.get(URL)
data = ''
if response.status_code == 200:
    data = response.content
print(data)
"""
"""
#QNO9
import pkg_resources
installed_ones = pkg_resources.working_set
for packages in installed_ones:
    print(packages)
"""
"""
#QNO10
import platform
submodules = [module[1] for module in platform(modules)]
print(submodules)
"""
"""
#QNO11
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70
ans = []
sum = 0
break_flag = False
for i in range(len(X)):
    for j in range(len(Y)):
        sum = X[i] + Y[j] + Z[j]
        if sum == target:
            ans.append(X[i])
            ans.append(Y[j])
            ans.append(Z[j])
            break_flag = True
            break
        if break_flag:
            break
print(ans)
"""
"""
#QNO12
nums = [11, 22, 33]
from itertools import permutations
nums1 = permutations(nums)
for i in nums1:
    print(i)
"""
"""
#QNO13
string_maps = {
"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}
from itertools import permutations
key_input = input("Key Input: ")
string_maps_needed = []
result = ''
for i in key_input:
    string_maps_needed.append(string_maps[i])
for i in range(len(string_maps_needed)+1):
    for k in range(len(string_maps_needed)+1):
        a = string_maps_needed[0][i]
        b = string_maps_needed[1][k]
        result = a + b
        print(result)
"""
"""
#QNO14
def add(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x

print(add(5, 81))
"""
"""
#QNO 15
def operators(operator1, operator2):
    operators_dict = { "+":1, "-":2, "*":3, "/":4
    }
    if operators_dict[operator1] > operators_dict[operator2]:
        return True
    else:
        return False

result = operators("*", "/")
print(result)
"""
"""
#QNO 16
def right_angle_triangle(opposite_side, adjacent_side, hypotenuse):
    result = 0
    if opposite_side == 'x':
        adjacent_side = adjacent_side ** 2
        hypotenuse = hypotenuse ** 2
        c = (adjacent_side + hypotenuse)
        result = math.sqrt(c)
    elif adjacent_side == 'x':
        opposite_side = opposite_side ** 2
        hypotenuse = hypotenuse ** 2
        c = (opposite_side + hypotenuse)
        result = math.sqrt(c)
    elif hypotenuse == 'x':
        opposite_side = opposite_side ** 2
        adjacent_side = adjacent_side ** 2
        c = (opposite_side + adjacent_side)
        result = math.sqrt(c)
    return result
res = right_angle_triangle(9, 'x', 11)
print(res)
"""
#QNO 17
#Missing
"""
#QNO 18
def median(n1, n2, n3):
    median_list = []
    median_list.append(n1)
    median_list.append(n2)
    median_list.append(n3)
    s = sorted(median_list)
    median_no = s[1]
    return median_no

result = median(2, 4 , 1)
print(result)
"""
"""
#QNO 19

string_num = input("Strings of Numbers: ")
num_list = []
answer = 0
n = 0
temp2 = 2
for i in range(len(string_num)):
    temp = int(string_num[i])
    if temp2 == 2:
        print(temp2)
    else:
        temp2 = temp2 ** 2
        print(temp2)
    else:
        n = n + 1
        temp2 = temp2 * n
"""
"""
#QNO 20
number = 5
quotient = number
trailing_zeros = 0
while quotient >= 5:
    quotient = int(quotient / 5)
    trailing_zeros = trailing_zeros + quotient
print(trailing_zeros)
"""
"""
#QNO 21
amount = 1000
remainder = 0
number_of_notes = 0
if amount >= 500:
    notes_of_five_hundreds = amount // 500
    number_of_notes = number_of_notes + notes_of_five_hundreds
    remainder = amount % 500
    #print("Five Hundred Notes: ", notes_of_five_hundreds)
if remainder >= 200:
    notes_of_two_hundreds = remainder // 200
    number_of_notes = number_of_notes + notes_of_two_hundreds
    remainder = remainder % 200
    #print("Two Hundred Notes: ", notes_of_two_hundreds)
    #print("remainder ", remainder)
if remainder >= 100:
    notes_of_one_hundreds = remainder // 100
    number_of_notes = number_of_notes + notes_of_one_hundreds
    remainder = remainder % 100
    #print("One Hundred Notes: ", notes_of_one_hundreds)
if remainder >= 50:
    notes_of_Fifties = remainder // 50
    number_of_notes = number_of_notes + notes_of_Fifties
    remainder = remainder % 50
    #print("Fifty Notes: ", notes_of_Fifties)
if remainder >= 20:
    notes_of_Twenties = remainder // 20
    number_of_notes = number_of_notes + notes_of_Twenties
    remainder = remainder % 20
    #print("Twenty Notes: ", notes_of_Twenties)
if remainder >= 10:
    notes_of_Tens = remainder // 10
    number_of_notes = number_of_notes + notes_of_Tens
    remainder = remainder % 10
    #print("Ten Notes: ", notes_of_Tens)

print("Total number of Notes: ", number_of_notes)
"""
"""
#QNO 22
number = int(input("Member sequence: "))
answer = 0
if number <= 4:
    print(1)
else:
    while number > 4:
        i = 0
        while i < 4:
            i = i + 1
            answer = (number-1) + answer
            print(answer)
            number = number - 1
            #print(number)
        #answer = answer + 1"""
"""
#QNO 23
number = input("Number: ")
s = 0
temp = int(number)
while temp > 0:
    for i in range(len(number)):
        s = s + int(number[i])
        #print(s)
        temp = temp - s
    temp = temp - s
    if temp > 0:
        print(temp)
"""
"""
#QNO 24
number = int(input("Number: " ))
temp = 0
for i in range(1, number+1):
    if (number % i) == 0:
        temp = temp + 1
    else:
        continue
print(temp)
"""
"""
#QNO 25
given_phone_number = input("Phone Numbers: ")
given_phone_number_list = [int(j) for j in given_phone_number]
original_numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
missing_numbers = []
for x in original_numbers_list:
    if x not in given_phone_number_list:
        missing_numbers.append(x)

print(missing_numbers)
"""
"""
#QNO26
numbers_Array = input("Numbers: ")
unique_list = []
from itertools import combinations
comb = combinations(numbers_Array, 2)
for i in list(comb):
    print(' '.join(i))
"""
"""
#QNO 27
sequence = input("Insert Sequence: ")
sequence_numbers = (sequence.split(","))
sequence_list_1 = [int(i) for i in sequence_numbers]
arithmetic_progression = False
Geometric_progression = False
diff = sequence_list_1[1] - sequence_list_1[0]
divisor = sequence_list_1[1] / sequence_list_1[0]
for x in range(1, len(sequence_list_1)):
    next_no = x + 1
    if next_no < len(sequence_list_1):
        if sequence_list_1[next_no] - sequence_list_1[x] == diff:
            arithmetic_progression = True
if arithmetic_progression:
    print("Arithmetic Progression")
    print("Next Sequence number is ", sequence_list_1[-1] + diff)
elif not arithmetic_progression:
    for k in range(1, len(sequence_list_1)):
        next_no1 = k + 1
        if next_no1 < len(sequence_list_1):
            if sequence_list_1[next_no1] / sequence_list_1[k] == divisor:
                Geometric_progression = True
    if Geometric_progression:
        print("Geometric Progression")
        print("Next Sequence number is ", sequence_list_1[-1] * divisor)
if arithmetic_progression != True and Geometric_progression != True:
    print("Wrong Sequence")
"""
"""
#QNO28
third_term = int(input("Input third term of the series:"))
third_term_last = int(input("Input 3rd last term:"))
sum_ofseries = 0
#Length_of_the_series = 0
series = []
for i in range(1, third_term+1):
    series.append(i)
    sum_ofseries = sum_ofseries + i
for k in range(third_term+1, third_term_last+3):
    series.append(k)
    sum_ofseries = sum_ofseries + k

print(series)
print(sum_ofseries)
"""
"""
#QNO29
pair = (input("Numbers: "))
pair_list = pair.split(",")
pair_list = [int(i) for i in pair_list]
max_no = max(pair_list)
result = 0
for i in range(2, max_no+1):
    if pair_list[0]/i == 0 and pair_list[1]/i == 0:
        result = i
        print(result)
    else:
        print("True")
"""
"""
@QNO 30
n = 1234
isPalindrome = False
result = 0
k = str(n)
n2 = [s for s in reversed(k)]
n3 = "".join(n2)
result = int(n) + int(n3)
result1 = str(result)
if result1 == result1[::-1]:
    isPalindrome = True
    print("Is Palindrome")
print(result1)
"""













