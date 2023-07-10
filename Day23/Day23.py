import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        if root is None:
            return
        
        outputQ = [root]
        while len(outputQ) != 0:
            out = outputQ.pop(0)
            print(out.data, end=" ")
            if out.left != None:
                outputQ.append(out.left)
            if out.right != None:
                outputQ.append(out.right)
            

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
