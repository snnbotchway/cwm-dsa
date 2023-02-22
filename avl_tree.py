class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self) -> str:
        return f"Node {self.value}"


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if not root:
            return Node(value)

        if value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        self.set_height(root)

        return self._balance(root)

    def set_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def _balance(self, root):
        if self._is_left_heavy(root):
            if self._balance_factor(root.left) < 0:
                root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        elif self._is_right_heavy(root):
            if self._balance_factor(root.right) > 0:
                root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _left_rotate(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        self.set_height(root)
        self.set_height(new_root)

        return new_root

    def _right_rotate(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        self.set_height(root)
        self.set_height(new_root)

        return new_root

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def _is_left_heavy(self, node):
        return self._balance_factor(node) > 1

    def _is_right_heavy(self, node):
        return self._balance_factor(node) < -1

    def height(self, node):
        if node is None:
            return -1
        return node.height

    # def _insert(self, root, value):
    #     print(f"Currently at {root.value}, do we go left or right?")
    #     if value < root.value:
    #         print("We go left!")
    #         if root.left:
    #             print(f"{root.left.value} is here, going there...")
    #             self._insert(root.left, value)
    #         else:
    #             root.left = Node(value)
    #             print(
    #                 f"{root.value} had no left child, {value} inserted as left child!\n")
    #             return
    #     elif value > root.value:
    #         print("We go right!")
    #         if root.right:
    #             print(f"{root.right.value} is here, going there...")
    #             self._insert(root.right, value)
    #         else:
    #             root.right = Node(value)
    #             print(
    #                 f"{root.value} had no right child, {value} inserted as right child!\n")
    #             return
    #     else:
    #         return


tree = AVLTree()
tree.insert(10)
tree.insert(30)
tree.insert(20)
# tree.insert(4)
# tree.insert(1)
# tree.insert(6)
# tree.insert(8)
# tree.insert(10)
