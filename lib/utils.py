#!/usr/bin/env python3

from collections import Counter
from time import time
from typing import Any

from lib.optimalBinarySearchTree import ObstNode

# from optimalBinarySearchTree import ObstNode


def print2D(root):
    COUNT = [10]

    def print2DUtil(root, space):
        # Base case
        if root == None:
            return

        # Increase distance between levels
        space += COUNT[0]

        # Process right child first
        print2DUtil(root.right, space)

        # Print current node after space
        # count
        print()
        for _ in range(COUNT[0], space):
            print(end=" ")
        key = f"{root.key[0:5]}.." if len(root.key) > 5 else root.key
        val = f"{root.value[0:5]}.." if len(root.value) > 5 else root.value
        node_label = [key, val]
        if hasattr(root, "freq"):
            node_label.append(root.freq)
        print(*node_label)

        # Process left child
        print2DUtil(root.left, space)

    # Pass initial space count as 0
    print2DUtil(root, 0)


def maxDepth(node):
    if node is None:
        return 0

    else:

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1


def time_it(func, *args, **kwargs) -> tuple[Any, float]:
    start: float = time()
    result: Any = func(*args, **kwargs)
    finish: float = start - time()
    print(result, finish)
    return (result, finish)


def txt_to_nodes(file_path: str):
    with open(file_path, "r") as f:
        data = f.read().splitlines()
        # print(data)
        d: dict[str, list[str]] = dict()
        l: list[str] = []
        for line in data:
            k, v = line.split("=")
            l.append(k)
            v = v.split(",")
            if d.get(k):
                d[k].extend(v)
            else:
                d[k] = v
        return [ObstNode(key, d[key], freq=freq) for key, freq in Counter(l).items()]


if __name__ == "__main__":
    print("Hello, welcome to the Optimal Binary Search Tree program!")
    txt_to_nodes("dictionary(english-chinese).txt")
    # time_it(find_optimal_binary_search_tree, t)
    # print2D(t.root)
