import sys

# Get the maximum integer value
MAX_INT = sys.maxsize
# Get the minimum integer value
MIN_INT = -sys.maxsize - 1


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
        node = Tree._Node(value)
        if self.root is None:
            self.root = node
            return
        current = self.root
        while True:
            if value > current.value:
                if current.right:
                    current = current.right
                    continue
                current.right = node
                break
            elif value < current.value:
                if current.left:
                    current = current.left
                    continue
                current.left = node
                break
            else:
                break
        # print(f"{value} inserted")

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

    def traverse_pre_order(self, root):
        if root is None:
            return
        print(root.value)
        self.traverse_pre_order(root.left)
        self.traverse_pre_order(root.right)

    def traverse_in_order(self, root):
        if root is None:
            return
        self.traverse_in_order(root.left)
        print(root.value)
        self.traverse_in_order(root.right)

    def traverse_post_order(self, root):
        if root is None:
            return
        self.traverse_post_order(root.left)
        self.traverse_post_order(root.right)
        print(root.value)

    def height(self, root):
        if root is None:
            return -1
        if root.left is None and root.right is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def min_node(self, root):
        if not root.left and not root.right:
            return root.value
        left = self.min_node(root.left)
        right = self.min_node(root.right)
        return min(left, right, root.value)

    def equals(self, tree):
        if not tree:
            return False
        return self._equals(self.root, tree.root)

    def _equals(self, self_node, other_node):
        if not self_node and not other_node:
            return True
        if self_node and other_node:
            return self_node.value == other_node.value and \
                self._equals(self_node.left, other_node.left) and \
                self._equals(self_node.right, other_node.right)
        return False

    def is_binary_search_tree(self, root, min=MIN_INT, max=MAX_INT):
        if not root:
            return True
        if root.value < min or root.value > max:
            return False
        return self.is_binary_search_tree(root.left, min, root.value - 1) and \
            self.is_binary_search_tree(root.right, root.value+1, max)

    def nodes_at_k_distance(self, root, k):
        if not root:
            return
        if k == 0:
            print(root.value)
            return
        self.nodes_at_k_distance(root.left, k-1)
        self.nodes_at_k_distance(root.right, k-1)


tree = Tree()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(6)
tree.insert(8)
tree.insert(10)
# print(tree.min_node(tree.root))
tree.nodes_at_k_distance(tree.root, 3)

# tree2 = Tree()
# tree2.insert(7)
# tree2.insert(4)
# tree2.insert(9)
# tree2.insert(1)
# tree2.insert(6)
# tree2.insert(8)
# tree2.insert(10)
# print(tree2.equals(tree))
