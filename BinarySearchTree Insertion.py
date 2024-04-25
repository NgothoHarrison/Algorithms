class Node:
    def __init__self(self, val):
        self.left = None
        self.right = None
        self.val = val

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)

def in_order_print(root):
    if 