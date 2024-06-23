from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS approach with TC-O(n) and SC-O(h)
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        # if root val more than high, discard right tree
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # if root val less than low, discard left tree
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root