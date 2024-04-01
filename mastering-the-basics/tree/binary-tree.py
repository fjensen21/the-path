class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = TreeNode(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = TreeNode(value)
        else:
            self.value = value


def printInOrder(root: TreeNode):
    if root.left:
        printInOrder(root.left)

    print(root)

    if root.right:
        printInOrder(root.right)


if __name__ == "__main__":
    root = TreeNode(5)
    root.insert(2)
    root.insert(6)
    root.insert(8)
    root.insert(8)
    root.insert(1)
    root.insert(4)

    printInOrder(root)
