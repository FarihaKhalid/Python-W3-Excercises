"""
for i in range(1, 11):
    if i == 10:
        break
    print(i, end=' ')
print("\nDone")
"""
from PIL.ImImagePlugin import number
from brlapi import rangeType_all
from jinja2.nodes import Continue
from xdg.IconTheme import themes

"""
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=' ')
print("\nDone")
"""
"""
i = 1
while i < 11:
    if i == 5:
        break
    i = i + 1
    print(i, end=' ')
    #i = i + 1
print("Done")
"""
"""
i = 1
while i < 11:
    if i % 2 == 0:
        i = i + 1
        continue
    print(i, end=" ")
    i = i + 1
#print("Done")
"""
"""
number = 10
while number > 0:
    print(number)
    number -=  2
"""
"""
i = 2
while i*i < 10:
    print(i)
    i = i + 1
print("done")
"""
"""
i = 2
while i * i < 10:
    print(i, end='\n')
    i = i + 1
print("Done")
"""
"""
for i in range(1, 11):
    if i == 5:
        print(i)
        break
print("Done")
"""
"""
for i in range(1, 11):
    if i%2 == 0:
        Continue
        print(i)
print("Done")
"""
"""
def next_fibonacci(threshold):
    a = 0
    b = 1
    c = 0
    while True:
        c = a + b
        #print(c)
        a = b
        #print(a)
        b = c
        #print(b)
        if c > threshold:
            print(c)
            break
        #print(c)
    return c
res = next_fibonacci(0)
"""
i = 3
while i > 1:
    print("Hello")
