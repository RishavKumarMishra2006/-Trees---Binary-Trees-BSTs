def leftView(root):
    result = []
    
    def helper(node, level):
        if not node:
            return
        
        if level == len(result):
            result.append(node.data)
        
        helper(node.left, level + 1)
        helper(node.right, level + 1)
    
    helper(root, 0)
    return result
