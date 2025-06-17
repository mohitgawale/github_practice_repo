import os

class TreeNode:
	def __init__(self,val = 0,left = None ,right = None):
		self.val = val 
		self.left = left
		self.right = right

	def __str__(self):
		left = str(self.left) if self.left else "None"
		right = str(self.right) if self.right else "None"
		return f"TreeNode({self.val}, L={left}, R={right})"

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


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (4 * level) + prefix + str(node.val))
        if node.left or node.right:
            print_tree(node.left, level + 1, prefix="L--- ")
            print_tree(node.right, level + 1, prefix="R--- ")
						
						
# inorder

def inorder(node):
	if not node:
		return
	inorder(node.left)
	print(node.val)
	inorder(node.right)

inorder(tree)

#preorder

def preorder(node):
	if not node:
		return
	print(node.val)
	preorder(node.left)
	preorder(node.right)

preorder(tree)


# postorder

def postorder(node):
	if not node:
		return
	postorder(node.left)
	postorder(node.right)
	print(node.val)

postorder(tree)

from collections import deque

def level_order(root):
    if not root:
        return

    queue = deque([(root, 0)])  # ✅ fix: no square brackets around root
    current_level = 0
    level_nodes = []

    while queue:
        node, level = queue.popleft()

        if level != current_level:
            print(f"Level {current_level}: {' '.join(map(str, level_nodes))}")
            level_nodes = []
            current_level = level

        level_nodes.append(node.val)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    # Print remaining nodes
    if level_nodes:
        print(f"Level {current_level}: {' '.join(map(str, level_nodes))}")

level_order(tree)