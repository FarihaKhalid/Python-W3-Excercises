"""
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers_length_four = []
for number in numbers:
    if len(number) == 4:
        numbers_length_four.append(number)
print(numbers_length_four)
"""
"""
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers_length_four = [no for no in numbers if len(no) == 4]
print(numbers_length_four)
"""
"""
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
comp_names = [name for name in names if 'e' in name]
print(comp_names)
"""
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_comp = [number for number in numbers if number % 2 == 0]
print(number_comp)
"""
"""
sentence = "The quick brown fox jumps over the lazy dog"
sentence_comp = [char for char in sentence if char.lower() in 'aeiou']
print(sentence_comp)
"""
"""
original_list = [1, 2, 3, 4, 5]
original_comp = [num ** 2 for num in original_list]
print(original_comp)
"""
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_comp = ['even' if number % 2 == 0 else 'odd' for number in numbers]
print(numbers_comp)
"""
"""
sentence = "Hello World! How are you doing?"
sentence_comp = [len(word) for word in sentence.split()]
print(sentence_comp)
"""
"""
def slice_and_Double(numbers, a, b):
    sliced_list = numbers[a:b+1]
    for number in numbers:
        poped = 
        
    return sliced_list
"""
"""
def slice_and_double(numbers, a, b):
    no = a
    double_no = 0
    j = 0
    if a < 0:
        a = 0
    sliced_num_list = numbers[a:b]
    double_sliced_num_list = []
    for i in range(len(sliced_num_list)):
        double_no = sliced_num_list[i] * 2
        double_sliced_num_list.append(double_no)
    for k in range(len(numbers)):
        if k in range(a, b):
            numbers.pop(k)
            s = double_sliced_num_list[j]
            numbers.insert(k, s)
            j = j + 1
    return numbers

result = slice_and_double([3, 6, 9, 12], -1, 3)
print("Output:", result)
"""
"""
def extract_odd_numbers(values):
    odd_values = [odd for odd in values if odd % 2 != 0]
    return odd_values
result = extract_odd_numbers([3, 6, 9, 1, 4, 15, 6, 3])
result1 = extract_odd_numbers([])
"""

words = ["apple", "banana", "cherry"]
words_f = [word[0] for word in words]
print(words_f)