#!/usr/bin/env python3

# This Python program implements an optimal binary search tree (abbreviated BST)
# building dynamic programming algorithm that delivers O(n^2) performance.
#
# The goal of the optimal BST problem is to build a low-cost BST for a
# given set of nodes, each with its own key and frequency. The frequency
# of the node is defined as how many time the node is being searched.
# The search cost of binary search tree is given by this formula:
#
# cost(1, n) = sum{i = 1 to n}((depth(node_i) + 1) * node_i_freq)
#
# where n is number of nodes in the BST. The characteristic of low-cost
# BSTs is having a faster overall search time than other implementations.
# The reason for their fast search time is that the nodes with high
# frequencies will be placed near the root of the tree while the nodes
# with low frequencies will be placed near the leaves of the tree thus
# reducing search time in the most frequent instances.
from __future__ import annotations

import sys
from collections import Counter
from dataclasses import dataclass

from lib.binarySearchTree import BstNode, BsTree


@dataclass
class ObstNode(BstNode):
    freq: int = 1
    """Binary Search Tree Node"""

    # def __str__(self):
    #     """
    #     >>> str(Node(1, 2))
    #     'Node(key=1, freq=2)'
    #     """
    #     return f"Node(key={self.key}, freq={self.freq})"


@dataclass
class ObsTree(BsTree):
    cost: int = 0


def find_optimal_binary_search_tree(nodes) -> BsTree:
    # Tree nodes must be sorted first, the code below sorts the keys in
    # increasing order and rearrange its frequencies accordingly.
    nodes.sort(key=lambda node: node.key)

    n: int = len(nodes)

    items: list[dict[str, str]] = [{nodes[i].key: nodes[i].value} for i in range(n)]
    freqs: list[int] = [nodes[i].freq for i in range(n)]

    # This 2D array stores the overall tree cost (which's as minimized as possible);
    # for a single key, cost is equal to frequency of the key.
    dp: list[list[int]] = [
        [freqs[i] if i == j else 0 for j in range(n)] for i in range(n)
    ]
    # sum[i][j] stores the sum of key frequencies between i and j inclusive in nodes
    # array
    total: list[list[int]] = [
        [freqs[i] if i == j else 0 for j in range(n)] for i in range(n)
    ]
    # stores tree roots that will be used later for constructing binary search tree
    root: list[list[int]] = [[i if i == j else 0 for j in range(n)] for i in range(n)]

    for interval_length in range(2, n + 1):
        for i in range(n - interval_length + 1):
            j = i + interval_length - 1

            dp[i][j] = sys.maxsize  # set the.key to "infinity"
            total[i][j] = total[i][j - 1] + freqs[j]

            # Apply Knuth's optimization
            for r in range(root[i][j - 1], root[i + 1][j] + 1):  # r is a temporal root
                left = dp[i][r - 1] if r != i else 0  # optimal cost for left subtree
                right = dp[r + 1][j] if r != j else 0  # optimal cost for right subtree
                cost = left + total[i][j] + right

                if dp[i][j] > cost:
                    dp[i][j] = cost
                    root[i][j] = r

    t = BsTree()

    def create_binary_search_tree_util(
        root: list[list[int]],
        items: list[dict[str, str]],
        i: int,
        j: int,
        parent: ObstNode | None,
        is_left: bool,
    ):

        if i > j or i < 0 or j > len(root) - 1:
            return

        node = root[i][j]
        key = [k for k in items[node].keys()][0]
        child = ObstNode(key, items[node][key], freq=freqs[node])
        if parent == None:  # root does not have a parent
            t.root = child
        elif is_left:
            parent.left = child
        else:
            parent.right = child

        create_binary_search_tree_util(root, items, i, node - 1, child, True)
        create_binary_search_tree_util(root, items, node + 1, j, child, False)

    create_binary_search_tree_util(root, items, 0, n - 1, None, False)
    return t


if __name__ == "__main__":
    # A sample binary search tree
    # nodes = [_Node(i, randint(1, 50)) for i in range(10, 0, -1)]

    f = {
        "e": "a",
        "c": "b",
        "g": "c",
        "b": "d",
        "d": "e",
        "f": "f",
        "h": "g",
        "a": "h",
        "i": "i",
        "j": "j",
    }
    d = ["e", "c", "g", "b", "d", "f", "h", "a", "i", "j", "j", "j", "j"]
    # print([(key, f[key], freq) for key, freq in Counter(d).items()])

    nodes = [ObstNode(key, f[key], freq=freq) for key, freq in Counter(d).items()]
    t = find_optimal_binary_search_tree(nodes)
    # print2D(t.root)
    # print(tuple((i.key, i.freq) for i in t.traversal_tree()))
