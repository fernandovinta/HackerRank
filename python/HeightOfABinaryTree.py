# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root, level = 0):
    if root is None:
        return 0;
    else:
        value = max([height(root.left, level + 1), height(root.right, level + 1)])
        return value if level == 0 else value + 1
