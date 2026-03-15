#! /usr/bin/env python3

from trees import *

binTree = BinTree(5)
#print(type(binTree.root))
binTree.setLeft(2)
binTree.setRight(10)
binTree.deleteItem
binTree.setItem(4)
#searchTree = SearchTree(10)

print(binTree.preorder())
print(binTree.inorder())
print(binTree.postorder())
print(binTree.levelorder())
#print(type(binTree))