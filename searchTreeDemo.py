#! /usr/bin/env python3

from searchtree import *

try: 
    errTree = SearchTree()
except TypeError as err:
    print(err)
tree = SearchTree(5)
print(tree.isEmpty())
tree.addItem(3)
tree.addItem(4)
tree.addItem(1)
tree.addItem(5)
tree.addItem(10)
tree.addItem(6)
tree.addItem(2)
tree.addItem(8)
tree.addItem(9)
tree.addItem(7)
print(tree.inorder())
print(tree.levelorder())
print(tree.getSubtree(10).inorder())