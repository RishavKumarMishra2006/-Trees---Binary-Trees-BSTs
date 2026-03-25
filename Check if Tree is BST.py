def isBST(root):
    def helper(node, low, high):
        if not node:
            return True
        
        if not (low < node.data < high):
            return False
        
        return (helper(node.left, low, node.data) and
                helper(node.right, node.data, high))
    
    return helper(root, float('-inf'), float('inf'))
