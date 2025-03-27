class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum(root):
    if not root:
        return 0
    
    res = 0
    queue = [(root, None)]
    
    while queue:
        node, parent = queue.pop(0)
        if not node.left and not node.right:
            if parent and parent.left == node:
                res += (node.data)
        if node.left:
            queue.append((node.left, node))
        if node.right:
            queue.append((node.right, node))
            
    return res

def insert_element(arr):
    if not arr:
        return None
    root = BinaryTree(int(arr[0]))
    queue = [root]
    i = 1
    while i < len(arr):
        curr = queue.pop(0)
        if curr:
            if arr[i] != "null":
                curr.left = BinaryTree(int(arr[i]))
                queue.append(curr.left)
            i+=1
            if i<len(arr) and arr[i] != "null":
                curr.right = BinaryTree(int(arr[i]))
                queue.append(curr.right)
            i+=1
    return root

n = int(input())
arr = input().split()
root = insert_element(arr)
print(sum(root))
