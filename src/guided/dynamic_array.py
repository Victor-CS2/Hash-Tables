class DynamicArray:
    def __init__(self, capacity=0):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity  # Allocate memory

    def insert(self, index, value):
        if self.count >= self.capacity:
            self.double_size()
        if index > self.count:
            print("ERROR: Out of range")
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]
        self.storage[index] = value
        self.count += 1

    def delete(self, index):
        if index >= self.count:
            print("Error: Out of range")
        for i in range(index, self.count-1, 1):
            self.storage[i] = self.storage[i+1]
        self.count -= 1

    def append(self, value):
        self.insert(self.count, value)

    def prepend(self, value):
        self.insert(0, value)

    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage


myArray = DynamicArray(3)
