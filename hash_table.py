from typing import List, Optional


class LinkedList:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None

    def add(self, key, value):
        node = self.head
        replaced = False
        while node:
            if node.key == key:
                node.value = value
                replaced = True  # update the value of the existing node
                return
            node = node.next

        # if the key was not found, add a new node
        new_node = LinkedList.Node(key, value)
        new_node.next = self.head
        self.head = new_node

        return replaced

    def remove(self, key):
        if self.head is None:
            return
        if self.head.key == key:
            value = self.head.value
            self.head = self.head.next
            return value
        else:
            current = self.head
            while current.next is not None and current.next.key != key:
                current = current.next
            if current.next is not None:
                value = current.next.key
                current.next = current.next.next
                return value
        raise Exception("No key found in this table.")

    def get(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None


class HashTable:
    def __init__(self) -> None:
        self.table: List[Optional[LinkedList]] = [None] * 5
        self.count = 0

    def _hash(self, key):
        return key % 5

    def _is_full(self):
        return self.count == 5

    def _is_empty(self):
        return self.count == 0

    def put(self, key, value):
        if self._is_full():
            raise Exception("This hashmap is full.")
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = LinkedList()
        replaced = self.table[index].add(key, value)
        if replaced is False:
            self.count += 1

    def remove(self, key):
        if self._is_empty():
            raise Exception("This hashmap is empty.")
        index = self._hash(key)
        list = self.table[index]
        removed_pair = list.remove(key)
        self.count -= 1
        return removed_pair

    def get(self, key):
        index = self._hash(key)
        node = self.table[index].head
        while node:
            if node.key == key:
                return node.value
            node = node.next

        return None

    def __str__(self) -> str:
        table = {}
        for list in self.table:
            if list is not None:
                current = list.head
                while current is not None:
                    table.update({current.key: current.value})
                    current = current.next
        return str(table)


table = HashTable()
table.put(1, "a")
table.put(11, "b")
table.put(13, "c")
table.put(16, "c")
table.put(1, "csdfihi")
table.put(2, "c")
print(table)
table.remove(2)
print(table)
