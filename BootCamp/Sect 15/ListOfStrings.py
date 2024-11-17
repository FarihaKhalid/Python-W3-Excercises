"""
def rotate_strings(strings, n):
    length_ofString  = len(strings)
    rotation = 0
    rotation_word = ''
    j = length_ofString -1
    if len(strings) > 0 and n > 0:
            while rotation < n:
                for i in range(length_ofString):
                    if rotation < n:
                        rotation_word = strings.pop(j)
                        strings.insert(0, rotation_word)
                        print("Rotation", rotation, "List ", strings)
                    rotation += 1
    else:
        return strings
    return strings
result = rotate_strings(['a', 'b', 'c'], 5)
print(result)
"""
from curses.ascii import isupper
from operator import attrgetter
from pickletools import string1
from reprlib import aRepr
from select import select

"""
def next_character(char):
    next_letter = chr(ord(char) + 1)
    print(f"Given Character {char}")
    print(f"Next Character {next_letter}")
    return next_letter
result = next_character('Y')
"""
"""
def encode_strings(strings):
    encoded_strings = []
    encoded_strings1 = []
    x = []
    for i in range(len(strings)):
        if i <= len(strings) <= 1000 and i <= len(strings[i]) <= 100:
            for l in strings[i]:
                former = ord(l)
                later = chr(former + 1)
                if former == 122:
                    later = chr(97)
                elif former == 90:
                    later = chr(65)
                encoded_strings.append(later)
                x = "".join(encoded_strings)
            encoded_strings.clear()
            encoded_strings1.append(x)
        if encoded_strings1 == [[]]:
            return ['']
    return encoded_strings1
result = encode_strings([''])
print(result)
"""
"""
def alternate_merge(list1, list2):
    merged_list = []
    biggest = []
    smallest = []
    if len(list1) > len(list2):
        biggest = list1
        smallest = list2
    else:
        biggest = list2
        smallest = list1
    if len(list1) > 0 or len(list2) > 0:
        for i in range(len(biggest)):
            if i < len(list1):
                merged_list.append(list1[i])
            if i < len(list2):
                merged_list.append(list2[i])
            else:
                continue
            print(merged_list)
    else:
        return list2
    return merged_list
result = alternate_merge([], [])
print(result)
"""
"""
class country:
    def __init__(self, name, area, population):
        self.name = name
        self.area = area
        self.population = population
    def __repr__(self):
        return repr((self.name, self.area, self.population))
countries = [country('Pakistan', 120,  1200),
             country("India", 200, 240),
             country(name="China", area=300, population=2000),
             country(name="Nepal", area=150, population=3000)]
print(countries)
countries.sort(key=attrgetter('population'), reverse=True)
print(countries)
print(max(countries, key=attrgetter('population')))
print(min(countries, key=attrgetter('population')))
print(max(countries, key=attrgetter('area')))
print(min(countries, key=attrgetter('area')))
"""
"""
def find_max(*args):
    max_value = args[0]
    for i in args:
        if i > max_value:
            max_value = i
    return max_value
result = find_max(3, 8, 2, 10, 5)
print(result)
"""
"""
def combine_strings(*args):
    return ''.join(args)
    #try1 = "".join(args)
    #return try1

result = combine_strings("Hello","World","There")
print(result)
"""
"""
def is_anagram(strings1, strings2):
    list1 = []
    list2  = []
    if len(strings1) != len(strings2):
        return False
    else:
        for i in range(len(strings1)):
            list1.append(strings1[i])
            list2.append(strings2[i])
    if list1 == list2:
        print("This is anagram")
    return True
result = is_anagram("apple", "ppale")
print(result)
"""
