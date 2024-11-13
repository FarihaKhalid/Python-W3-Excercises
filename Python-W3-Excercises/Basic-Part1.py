"""
#QNO1
print("Twinkle, twinkle, little star,\n""\t How I wonder what you are!\n""\t\t Up above the world so high,\n"
      "\t\tLike a diamond in the sky.""\nTwinkle, twinkle, little star,\n""\tHow I wonder what you are")
"""
from audioop import reverse

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
#QNO6
data = 3, 5, 7, 23
data2 = data
data_list = []
for i in data:
      if i == ' ' or i  == ",":
            pass
      else:
            data_list.append(f'{i}')
my_tuple = tuple(data_list)
print(data_list)
print(my_tuple)


