class Solution:
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    # Helper function: Same Binary Tree
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )

# Time: O(n * m) — search × comparison
# Space: O(h) — recursion stack