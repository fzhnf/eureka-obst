#!/usr/bin/env python3

from os import get_terminal_size

from lib.binarySearchTree import BsTree
from lib.optimalBinarySearchTree import find_optimal_binary_search_tree
from lib.utils import maxDepth, print2D, time_it, txt_to_nodes

print("Hello, welcome to the Optimal Binary Search Tree program!")
print("Binary Search Tree vs Optimal Binary Search Tree")
do = txt_to_nodes("dictionary(english-chinese).txt")
d = dict()
for data in do:
    d[data.key] = data.value
t = BsTree().insert(**d)
to = find_optimal_binary_search_tree(do)

term_size = get_terminal_size()
print()
print()
print()
print("-" * term_size.columns)
print("tree structure differences:")
print("BST:")
print2D(t.root)
print("-" * term_size.columns)
print("Optimal BST:")
print2D(to.root)
print()
print()
print()
print("-" * term_size.columns)
print("search time differences: keyword = 'indian'")
result1, time1 = time_it(t.search, "indian")
result2, time2 = time_it(to.search, "indian")
print(f"BST: {result1.key} = {result1.value} found in {time1:.10f} seconds")
print(f"Optimal BST: {result2.key} = {result2.value} found in {time2:.10f} seconds")
print()
print()
print()
print("-" * term_size.columns)
print("height differences:")
t_height = maxDepth(t.root)
to_height = maxDepth(to.root)
print(f"BST highest height: {t_height}")
print(f"OBST highest height: {to_height}")
