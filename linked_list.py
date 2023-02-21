

class LinkedList:
    class Node:
        def __init__(self, value) -> None:
            self.value = value
            self.next = None

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.count = 0
        self.array = []

    def _is_empty(self):
        return self.first is None

    def add_first(self, item):
        node = LinkedList.Node(item)
        if self._is_empty():
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node
        self.count += 1

    def add_last(self, item):
        node = LinkedList.Node(item)
        if self._is_empty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.count += 1

    def index_of(self, value):
        current = self.first
        index = 0
        while current is not None:
            if current.value == value:
                return index
            index += 1
            current = current.next
        return -1

    def contains(self, value):
        return self.index_of(value) != -1

    def remove_first(self):
        if self._is_empty():
            raise Exception("This list is empty.")
        first = self.first
        if self.first == self.last:
            removed_value = self.first.value
            self.first = self.last = None
            self.count -= 1
            return removed_value
        self.first = self.first.next
        first.next = None
        self.count -= 1
        return first.value

    def remove_last(self):
        if self._is_empty():
            raise Exception("This list is empty.")
        if self.first == self.last:
            removed_value = self.first.value
            self.first = self.last = None
            self.count -= 1
            return removed_value
        last_but_one = self._get_previous_node(self.last)
        removed_value = self.last.value
        self.last = last_but_one
        last_but_one.next = None
        self.count -= 1
        return removed_value

    def _get_previous_node(self, node):
        current = self.first
        while current.next != node:
            if current.next is None:
                return None
            current = current.next
        return current

    def size(self):
        return self.count

    def to_array(self):
        array = []
        current = self.first
        while current is not None:
            array.append(current.value)
            current = current.next
        return array

    def reverse(self):
        if self._is_empty():
            return
        prev = self.first
        current = self.first.next
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.last = self.first
        self.last.next = None
        self.first = prev

    def get_kth_from_the_end(self, k):
        if self._is_empty():
            raise Exception("This list is empty.")
        if k < 1:
            raise ValueError("k cannot be less than one.")
        last_pointer = target_pointer = self.first
        for _ in range(k-1):
            last_pointer = last_pointer.next
            if last_pointer is None:
                raise ValueError(
                    "k cannot be greater than the length of the list")
        while last_pointer.next is not None:
            last_pointer = last_pointer.next
            target_pointer = target_pointer.next
        return target_pointer.value


# l_list = LinkedList()
# # l_list.add_last(10)
# print(l_list.to_array())
# print(l_list.get_kth_from_the_end(5))
