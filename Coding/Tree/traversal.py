from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# tree preorder traversal (V-L-R)
def preorder(root: TreeNode) -> None:
    if not root: return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# tree inorder traversal (L-V-R)
def inorder(root: TreeNode) -> None:
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# tree postorder traversal (L-R-V)
def preorder(root: TreeNode) -> None:
    if not root: return
    preorder(root.left)
    preorder(root.right)
    print(root.val)

# level order traversal (BFS)
def levelorder(root: TreeNode) -> None:
    if not root: return
    que = deque([root])

    while que:
        size = len(que)

        for i in range(size):
            node = que.popleft()
            print(node.val)

            if node.left: que.append(node.left)
            if node.right: que.append(node.right)