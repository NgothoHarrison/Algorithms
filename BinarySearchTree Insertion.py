class Node:
    def __init__self(self, val):
        self.left = None
        self.right = None
        self.val = val

def insert(root, val):
    if root is None:
        return Node(val)
    else:
        if root.val < val:
            root.right = insert(root.right, val)
        else:
            root.left = insert(root.left, val)
    return root