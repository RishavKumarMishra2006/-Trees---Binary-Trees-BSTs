def diameter(root):
    res = 0
    
    def height(node):
        nonlocal res
        if not node:
            return 0
        
        lh = height(node.left)
        rh = height(node.right)
        
        res = max(res, lh + rh)
        
        return max(lh, rh) + 1
    
    height(root)
    return res
