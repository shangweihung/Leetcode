from collections import defaultdict

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def verticalOrder(self,root):
        result=[]
        if not root:
            return result

        queue=[(root,1)]
        HashMap=defaultdict(list)
        
        while queue:
            
            node=queue.pop(0)
            HashMap[node[1]].append(node[0].val)

            left,right=node[0].left,node[0].right

            if left:
                queue.append((left,node[1]-1))

            if right:
                queue.append((right,node[1]+1))

        for i in sorted(HashMap.keys()):
            result.append(HashMap[i])
        return result




if __name__=="__main__":
    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right= n5
    
    print(Solution().verticalOrder(n1)==[[9],[3,15],[20],[7]])


    h1 = TreeNode(3)
    h2 = TreeNode(9)
    h3 = TreeNode(8)
    h4 = TreeNode(4)
    h5 = TreeNode(0)
    h6 = TreeNode(1)
    h7 = TreeNode(7)
    h8 = TreeNode(5)
    h9 = TreeNode(2)

    h1.left = h2
    h1.right = h3
    h2.left = h4
    h2.right = h5
    h3.left = h6
    h3.right= h7
    h5.left = h8
    h5.right = h9

    print(Solution().verticalOrder(h1)==[[4],[9,5],[3,0,1],[8,2],[7]])
