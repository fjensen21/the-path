class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    

def serialize(root):
    result = []

    def dfs(node):
        if not node:
            result.append("N")
            return
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ",".join(result)

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


if __name__ == "__main__":
    # Test Case 1
    root = deserialize("1,2,N,N,3,4,N,N,5,N,N")

    # Serialize test case
    string_version = serialize(root)
