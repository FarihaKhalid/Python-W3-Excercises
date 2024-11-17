"""
class queue:
    def __init__(self):
        self.items = []

    def enqueue_element(self, item):
        self.items.append(item)
        return self.items

    def is_empty(self):
        ans = ''
        if len(self.items) == 0:
            ans = True
        else:
            ans = False
        return ans

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def front_element(self):
        if len(self.items) > 0:
            return self.items[0]

    def display(self):
        return self.items

result = queue()
print(result.enqueue_element(1))
print(result.enqueue_element(2))
print(result.enqueue_element(3))
print(result.enqueue_element(4))
print("Is Empty",result.is_empty())
print("Remove first element",result.dequeue())
print("Front ",result.front_element())
print("Display", result.display())
"""