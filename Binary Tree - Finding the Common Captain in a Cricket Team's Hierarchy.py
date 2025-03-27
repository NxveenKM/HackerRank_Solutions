class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
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
            i += 1
            if i < len(arr) and arr[i] != "null":
                curr.right = BinaryTree(int(arr[i]))
                queue.append(curr.right)
            i += 1
    return root

def findLCA(root, a, b):
    if not root:
        return None
    if root.data == a or root.data == b:
        return root
    
    leftLCA = findLCA(root.left, a, b)
    rightLCA = findLCA(root.right, a, b)
    
    if leftLCA and rightLCA:
        return root
    return leftLCA if leftLCA else rightLCA

n = int(input())
arr = input().split()
a, b = map(int, input().split())
root = insert_element(arr)
lca_node = findLCA(root, a, b)

print(lca_node.data)
