class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def deserialize(data):
    vals = data.split(",")

    def dfs(i):
        if vals[i] == "N":
            i += 1
            return None, i
        node = TreeNode(int(vals[i]))
        i += 1
        node.left, i = dfs(i)
        node.right, i = dfs(i)
        return node, i

    node, _ = dfs(0)
    return node


def max_path_sum(root):
    result = [root.val]

    # Returns the max with no splitting while also
    # updating result to be the max with a split from any node
    def dfs(root):
        if not root:
            return 0

        left_max = dfs(root.left)
        right_max = dfs(root.right)
        left_max = max(left_max, 0)
        right_max = max(right_max, 0)

        # compute max path sum WITH split
        result[0] = max(result[0], root.val + left_max + right_max)

        return root.val + max(left_max, right_max)

    dfs(root)
    return result[0]


if __name__ == "__main__":
    root = deserialize("1,2,N,N,3,4,N,N,5,N,N")
    print("Max Path Sum: ", max_path_sum(root))
