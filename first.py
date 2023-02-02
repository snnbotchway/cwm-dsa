class Array:
    def __init__(self, length) -> None:
        self.contents = [None] * length
        self.length = 0

    def print(self):
        for item in self.contents:
            if item is not None:
                print(item)

    def insert(self, item):
        # Store contacts in temporary variable
        temp = self.contents
        # Increase length of array by 1
        self.length += 1
        # create empty array of new length
        self.contents = [None] * self.length
        #
        for index in range(self.length-1):
            if index < self.length - 1:
                self.contents[index] = temp[index]
            else:
                self.contents[index] = item

    def removeAt(self, index):
        self.contents[index] = None
        temp = self.contents
        self.length -= 1
        self.contents = [None] * self.length
        index = 0
        for item in temp:
            if item is not None:
                self.contents[index] = item
                index += 1


numbers = Array(3)
numbers.insert(10)
numbers.insert(20)
numbers.insert(30)
numbers.print()
