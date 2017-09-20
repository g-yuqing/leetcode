class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        nodelist = [root]
        while nodelist:
            childlist = []
            temp_res = []
            for node in nodelist:
                temp_res.append(node.val)
                if node.left:
                    childlist.append(node.left)
                if node.right:
                    childlist.append(node.right)
            res.append(temp_res)
            nodelist = childlist[:]
        return res
