# Given a binary tree, each node has value 0 or 1.
# Each root-to-leaf path represents a binary number starting with the most significant bit.
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
# Return the sum of these numbers.

# Example 1:
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


# Note:
# The number of nodes in the tree is between 1 and 1000.
# node.val is 0 or 1.
# The answer will not exceed 2^31 - 1.

# Definition for a binary tree node.
from functools import reduce
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getPathListFromNode(self, node: TreeNode) -> List[str]:
        if node == None or node.val == None:
            return []
        if node.left == None and node.right == None:
            return [str(node.val)]
        rightPath = [str(node.val)+leafString for leafString in self.getPathListFromNode(
            node.right)] if node.right != None else []
        leftPath = [str(node.val)+leafString for leafString in self.getPathListFromNode(
            node.left)] if node.left != None else []
        return rightPath+leftPath

    def sumRootToLeaf(self, root: TreeNode) -> int:
        pathList = self.getPathListFromNode(root)
        return reduce(lambda x, y: x+int(y, 2), pathList, 0)


s = Solution()
print(s.sumRootToLeaf([0,1,1]))
