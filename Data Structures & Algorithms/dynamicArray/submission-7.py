class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.store = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.store[i]

    def set(self, i: int, n: int) -> None:
        self.store[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.store[self.length] = n
        self.length += 1    

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.store[self.length]    

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity

        for i in range(self.length):
            new_arr[i] = self.store[i]
        self.store = new_arr    

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity