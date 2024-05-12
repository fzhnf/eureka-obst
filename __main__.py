#!/usr/bin/env python3


from lib.binarySearchTree import BsTree
from lib.optimalBinarySearchTree import find_optimal_binary_search_tree
from lib.utils import print2D, time_it, txt_to_nodes

print("Hello, welcome to the Optimal Binary Search Tree program!")
do = txt_to_nodes("dictionary(english-chinese).txt")
d = dict()
for data in do:
    d[data.key] = data.value
t = BsTree().insert(**d)
to = find_optimal_binary_search_tree(do)
print(to)
print(t)

print2D(t.root)
print2D(to.root)

result1, time1 = time_it(t.search, "japanese")
result2, time2 = time_it(to.search, "japanese")
print(result1, time1)
print(result2, time2)


# print("Binary search tree nodes:")
# print("Optimal binary search tree nodes:")
# while True:
#     print(
#         """
#     1. compare the tree in visual
#     2. compare search time
#     3. Exit
#     """
#     )
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         print("Binary search tree:")
#         print2D(t.root)
#         print("Optimal binary search tree:")
#         print2D(to.root)
#     elif choice == "2":
#         a = str(input("Enter the key to search: "))
#         result1, time1 = time_it(t.search, a)
#         result2, time2 = time_it(to.search, a)
#         print(f"result1: {result1.value} found in {time1} seconds")
#         print(f"result2: {result2.value} found in {time2} seconds")
#     elif choice == "3":
#         print("Thanks for using the program!")
#         break
#     else:
#         print("Invalid choice. Please try again.")
#         continue
