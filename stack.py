
class Stack:
    def __init__(self, size) -> None:
        self.stack = [None]*size
        self.count = 0

    def push(self, value):
        self.stack.append(value)
        self.count += 1

    def pop(self):
        if (self.is_empty()):
            raise Exception("This stack is empty")
        popped = self.stack.pop()
        self.count -= 1
        return popped

    def peek(self):
        if (self.is_empty):
            raise Exception("This stack is empty")
        return self.stack[self.count-1]

    def is_empty(self):
        return self.count == 0

    def print(self):
        return self.stack


def reverse(string):
    if string is None:
        raise ValueError("input string cannot be null")
    stack = Stack()
    for char in string:
        stack.push(char)
    return "".join([stack.pop() for _ in range(stack.count)])


left_brackets = "({[<"
right_brackets = ")}]>"


def is_balanced(string):
    stack = Stack()

    for char in string:
        if _is_left_bracket(char):
            stack.push(char)

        if _is_right_bracket(char):
            if stack.is_empty():
                return False

            left = stack.pop()
            if not _brackets_match(left=left, right=char):
                return False

    return stack.is_empty()


def _is_left_bracket(char):
    return char in left_brackets


def _is_right_bracket(char):
    return char in right_brackets


def _brackets_match(left, right):
    return left_brackets.index(left) == right_brackets.index(right)


print(is_balanced("<asg>"))
