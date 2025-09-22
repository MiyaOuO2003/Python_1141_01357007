class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTreePreIn(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    inorder_index = inorder.index(root_val)

    root.left = buildTreePreIn(
        preorder[1 : 1 + inorder_index],  # Preorder for left subtree
        inorder[:inorder_index]           # Inorder for left subtree
    )
    root.right = buildTreePreIn(
        preorder[1 + inorder_index:],     # Preorder for right subtree
        inorder[inorder_index + 1:]       # Inorder for right subtree
    )
    return root

def treeHeight(root):
    if root is None:
        return 0
    return 1 + max(treeHeight(root.left), treeHeight(root.right))

po = list(map(int, input().split()))
io = list(map(int, input().split()))

root = buildTreePreIn(po, io)
print(treeHeight(root))