# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxSum=float("-inf")

        def gain(curr):
            if not curr:
                return 0
            
            left=max(gain(curr.left),0)
            right=max(gain(curr.right),0)
            maxPath=curr.val+left+right
            self.maxSum=max(self.maxSum,maxPath)
            return curr.val+ max(left,right)
        gain(root)
        return self.maxSum

        