import os

class TreeNode:
  def __init__(self,val = 0,left = None ,right = None):
    self.val = val 
    self.left = left
    self.right = right
  
  def __str__(self):
      return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
  
root = TreeNode(1)
root.left = TreeNode(2)


def build_tree(values, index=0):
    if index >= len(values) or values[index] is None:
        return None
    
    node = TreeNode(values[index])
    node.left = build_tree(values, 2 * index + 1)
    node.right = build_tree(values, 2 * index + 2)
    return node

tree = build_tree([1, 2, 3, 4, 5])

