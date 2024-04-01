#BFS template
def bfs(root: TreeNode) -> None:
    if not root: return
    q = deque([root])
    
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            print(str(node.val), end = " ")
            #PROCESS HERE
            if node.left: 
                q.append(node.left)
            if node.right: 
                q.append(node.right)

        print()

#DFS template
def preorder(root: TreeNode) -> None:
    if not root: return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def inorder(root: TreeNode) -> None:
    if not root: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def postorder(root: TreeNode) -> None:
    if not root: return
    postorder(root.left)
    postorder(root.right)
    print(root.val)


#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#use DFS
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None #invalid case, so if that branch return none we know it is not have p or q
        
        if root == p or root == q:
            return root #valid case, if that branch return a value we know that it have either p or q

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # if both left and right subtrees return a valid node, the current node is the lowest common ancestor
        if l and r:
            return root

        return l or r # if 1 of them valid that mean it have both, this is the example 2 case

#https://leetcode.com/problems/path-sum/
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    ans = False
    if root is None:
        return False
    def dfs(node, total):
        nonlocal ans
        if node is None:
            return
        if node.left is None and node.right is None and total+node.val == targetSum:
            ans = True
        dfs(node.left, total + node.val)
        dfs(node.right, total + node.val)
    dfs(root,0)
    return ans


# 102. Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        q = deque([root])
        ans = []
        i=0
        
        while q:
            size = len(q)
            temp = []
            for i in range(size):
                node = q.popleft()
                # print(str(node.val), end = " ")
                temp.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            ans.append(temp)
            # print()
        return ans

