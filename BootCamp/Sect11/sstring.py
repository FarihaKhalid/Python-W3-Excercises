"""
message = "Hello World"
print(type(message))
"""
from importlib.util import resolve_name
from itertools import chain

from louis import charSize
from reportlab.graphics.barcode.eanbc import words
from reportlab.platypus.paragraph import split

"""
message = "hello"
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.casefold())
print(message.islower())
print(message.isupper())
"""
"""
print(message.istitle())
print(message.title())
print(message.islower())
print(message.isnumeric())
print(message.isupper())
"""
"""
print("2 3".isdigit())
print('233'.isalnum())
print('A123'.isalpha())
"""
"""
print('Hello World'.endswith('World'))
print('Hello World'.startswith('Hello'))
print('')
"""
"""
print(res.find('b'))
print('b' in res)
"""
"""
message = 'Hello World'
print(message[0])
print(type(message[0]))
#print(type (message[100]))
for chr in message:
    print(chr)
"""
"""
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.hexdigits)
print(string.digits)
print(string.punctuation)
"""
"""
for chr in string.punctuation:
    print(chr,'\n')"""
"""
for chr in string.ascii_uppercase:
    print(chr)"""
"""
str = 'test'
str2 = 'Test'
print(str == str2)
print(str > str2)
print(str < str2)
print(str != str2)
"""
"""
str = 'Python'
str2 = 'python2'
print(str.upper() == str2.upper())
print(str.lower() == str2.lower())
print(ord(str[0]))
print(ord(str2[0]))
"""
"""
def is_vowel(char):
    vowels = 'aeiouAEIOU'
    condition = ''
    if char in vowels:
        condition = True
    else:
        condition = False
    return condition
print(is_vowel('A'))
"""
"""
def count_uppercase_letters(text):
    count = 0
    chr = ''
    for chr in text:
        if chr.isupper():
            print(chr)
            count = count + 1
    return count
print(count_uppercase_letters('AEgh'))
"""
"""
def has_consecutive_identical_characters(text):
    sec = len(text) - 1
    cond = False
    for i in range(0, sec):
        third = i + 1
        if text[i] == text[third]:
            #print(text[i], text[third])
            cond = True
    return cond
res = has_consecutive_identical_characters('I love Switzerland')
print(res)
"""
"""
def find_right_most_digit(text):
    chr = -1
    for chr in reversed(text):
        if chr.isdigit():
            print(chr)
            break
        else:
            chr = -1
            print(chr)
    return int(chr)
res = print(find_right_most_digit('42'))
"""
"""
def find_longest_word(text):
    res = text.split()
    c = ''
    c_word = 0
    n_word = 0
    for word in res:
        #n_word = c_word
        c_word = len(word)
        if c_word > n_word:
            n_word = c_word
            c = word
        else:
            continue
    return c
result = (find_longest_word('The quick brown fox jumps over the lazy dog'))
print(result)
"""
"""
def is_anagram(string1, string2):
    s1 = sorted(string1)
    s2 = sorted(string2)
    if s1 == s2:
        return True
    else:
        return False
res = print(is_anagram('hello', 'hello'))
"""
"""
def is_hex_string(string1):
    hex_digit = '0123456789abcdefABCDEF'
    bol = False
    for chr in string1:
        if chr in hex_digit:
            bol = True
            #print("This is True", chr)
        else:
            bol = False
            #print("This is false", chr)
            break
    return bol
res = is_hex_string('1g2f4C')
print(res)
"""
"""
def reverse_word(word):
    reversed_w = word.split()
    s = 0
    w = ''
    for i in range(0, len(word)):
        s = (len(word)-1) - i
        w = w + word[s]
    return w
res = reverse_word("Python")
print(res)
"""
"""
data_type = "Hello World"
print(type(data_type))

char = 'A'
count = 0
for c in "ABRACADABRA":
    if c == char:
        count += 1
print(count)
"""
"""
str1 = "apple"
str2 = "banana"
print(str1 < str2)
"""
"""
text = 'Python'
repeated_text = text * 3
print(repeated_text)
"""
"""
str1 = "Hello"
str2 = "World"
print(str1+str2)
"""
"""
str1 = "Hello"
str2 = "World"
print(len(str1) == len(str2))
print(len(str1) + len(str2))
"""
"""
print('1' * 20)
print(1 * 20)
print(type('ABCB' * 20))
"""
"""
print('Python'.find('py'))
print('HELLO'.isupper())
print('Py'in'Python')
"""






