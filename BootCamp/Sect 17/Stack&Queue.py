"""
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
print(numbers)

numbers.pop(-1)
print(numbers)

print(numbers[2])

print("Is stack empty", bool(numbers))
"""
"""
class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return self.items

    def is_empty(self):
        self.is_empty1 = True
        if len(self.items) == 0:
            return True
        else:
            return False

    def pop1(self, item):
        if self.is_empty1:
            self.items.pop(item)
            return self.items

    def top1(self):
        if self.is_empty1:
            return self.items[-1]

    def display(self):
        return self.items

result = stack()
print(result.push(2))
print(result.push(4))
print(result.is_empty())
print(result.top1())
print(result.display())
print(result.pop1(0))
"""
"""
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)

print("Dequeued element", numbers.pop(0))

print("Queue after enqueues", numbers)

print("Front of queue", numbers[0])

print("Is queue empty", not bool(numbers))
"""
