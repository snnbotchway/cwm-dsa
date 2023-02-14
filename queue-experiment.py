from collections import deque
# queue = deque()
# print(queue.popleft())


def reverse(queue: deque):
    stack = []
    while queue:
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())
    return queue


class ArrayQueue:
    def __init__(self, capacity):
        self.items = [None]*capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise Exception("This queue is full.")
        self.items[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("This queue is empty.")
        removed = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return removed

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    def __str__(self):
        front = self.front
        return str([self.items[(front + i) % self.capacity] for i in range(self.size)])


class StackQueue:
    def __init__(self, capacity):
        self.input = []
        self.output = []
        self.capacity = capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def _reverse_input_into_output(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

    def enqueue(self, value):
        if self.is_full():
            raise Exception("This queue is full.")
        # self._reverse_input_into_output()
        self.input.append(value)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("This queue is empty.")
        self._reverse_input_into_output()
        self.size -= 1
        return self.output.pop()

    def peek(self):
        if self.is_empty():
            return None
        self._reverse_input_into_output()
        return self.output[-1]

    def __str__(self):
        items = []
        for _ in range(self.size):
            self._reverse_input_into_output()
            items.append(self.output.pop())
        return str(items)


class PriorityQueue:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise Exception("This queue is full.")
        if self.is_empty():
            self.items.append(value)
            self.size += 1
            return
        if self.size == 1:
            if value >= self.items[0]:
                self.items.append(value)
                self.size += 1
                return
            else:
                self.items.append(None)
                self.items[1] = self.items[0]
                self.items[0] = value
                self.size += 1
                return

        i = self.size - 1
        self.items.append(None)

        while (i >= 0):
            if self.size > 2:
                print(i, self.items)
            if value < self.items[i]:
                self.items[i+1] = self.items[i]
            else:
                break
            i -= 1
        self.items[i+1] = value
        self.size += 1

    # def dequeue(self):
    #     if self.is_empty():
    #         raise IndexError("This queue is empty.")
    #     self._reverse_input_into_output()
    #     self.size -= 1
    #     return self.output.pop()

    # def peek(self):
    #     if self.is_empty():
    #         return None
    #     self._reverse_input_into_output()
    #     return self.output[-1]

    def __str__(self):
        return str(self.items)


queue = PriorityQueue(10)
queue.enqueue(25)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(70)
# queue.enqueue(50)
# queue.dequeue()
# queue.dequeue()
# queue.enqueue(40)
# queue.enqueue(50)
# queue.dequeue()
# queue.dequeue()
# queue.enqueue(60)
# queue.enqueue(70)
# print(queue.peek())
print(queue)
