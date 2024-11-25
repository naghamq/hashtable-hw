class HashTable:
    def __init__(self):
        self.size=size
        self.array=[None]*size

    def get(self, key):
        index=(key)%self.size
        return self.array[index]

    def set(self, key, value):
        index=(key)%self.size
        self.array[index] = value

# Example usage
table = HashTable(5)
table.set(238, "hello")  # 238 % 5 = 3
table.set(5251, "world")  # 5251 % 5 = 1
table.set(123, "good")  # 123 % 5 = 3 (collision with 238)

# Retrieving values
print(table.get(238))   # Output: good (because 123 overwrote the value at index 3)
print(table.get(5251))  # Output: world
print(table.get(22))    # Output: None (no value at 22 % 5 = 2)

