from collections import deque

def levelOrder(root):
    if not root:
        return
    
    q = deque([root])
    
    while q:
        node = q.popleft()
        print(node.data, end=" ")
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
