# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Empty node: O(1)
        if not root:
            return 0

        # TIME: Each node is visited once
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # O(1): Compare two values and add 1
        return 1 + max(left, right)


# TIME: O(n)  → Visit all n nodes once
# SPACE: O(h) → Recursion stack follows tree height