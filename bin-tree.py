class Tree:
    class _Node:
        def __init__(self, value) -> None:
            self.value = value
            self.left = None
            self.right = None

        def __str__(self) -> str:
            return f"Node {self.value}"

    def __init__(self, root=None) -> None:
        self.root = root

    def insert(self, value):
        if self.root is None:
            self.root = Tree._Node(value)
            return
        current = self.root
        while True:
            if value > current.value:
                if current.right:
                    current = current.right
                if current.right:
                    current.right = Tree._Node(value)
                    break
            elif value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Tree._Node(value)
                    break
            else:
                break

    def find(self, value):
        if self.root is None:
            print("The list sef empty lol...")
            return False
        current = self.root
        print(f"Looking for for {value}")
        while True:
            print(
                f"Currently at node {current.value}. Do we go left or right?")
            if value > current.value:
                if current.right:
                    current = current.right
                    print("We go right!")
                else:
                    print("Not found lol...\n")
                    return False
            elif value < current.value:
                if current.left:
                    current = current.left
                    print("We go left!")
                else:
                    print("Not found lol...\n")
                    return False
            else:
                print(f"{value} found we no go go anywhere tsw\n")
                return True

    def traverse_pre_order(self):
        self._traverse_pre_order(self.root)

    def _traverse_pre_order(self, root):
        print(root.value)
        if root is None:
            return
        self._traverse_pre_order(root.left)
        self._traverse_pre_order(root.right)


tree = Tree()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(6)
tree.insert(8)
tree.insert(10)
tree.traverse_pre_order()
