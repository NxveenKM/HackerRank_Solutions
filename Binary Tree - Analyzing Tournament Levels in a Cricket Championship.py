class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def maxDepth(root):
    if not root:
        return 0
    else:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        return max(left_depth, right_depth) + 1

def buildTree(level_order):
    if not level_order or level_order[0] == "null":
        return None
    
    root = TreeNode(level_order[0])
    queue = [root]
    index = 1
    
    while queue and index < len(level_order):
        current = queue.pop(0)
        
        if index < len(level_order) and level_order[index] != "null":
            current.left = TreeNode(level_order[index])
            queue.append(current.left)
        index += 1
        
        if index < len(level_order) and level_order[index] != "null":
            current.right = TreeNode(level_order[index])
            queue.append(current.right)
        index += 1
    
    return root

n = int(input().strip())
level_order = input().strip().split()

root = buildTree(level_order)

depth = maxDepth(root)

print(depth)
