def minValueNode(root):
    while root.left:
        root = root.left
    return root

def deleteNode(root, key):
    if not root:
        return root
    
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        # Case 1 & 2
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # Case 3: Two children
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    
    return root
