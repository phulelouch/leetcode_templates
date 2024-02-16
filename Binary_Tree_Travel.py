#BFS template
def bfs(root: TreeNode) -> None:
    if not root: return
    q = deque([root])
    
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            print(str(node.val), end = " ")
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
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root

    l = self.lowestCommonAncestor(root.left, p, q)
    r = self.lowestCommonAncestor(root.right, p, q)

    if l and r:
        return root
    return l or r


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
