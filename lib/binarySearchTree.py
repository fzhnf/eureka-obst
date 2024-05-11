#!/usr/bin/env python3

from __future__ import annotations

import sys
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Self

from utils import print2D, time_it


@dataclass
class BstNode:
    value: str
    left: BstNode | None = None
    right: BstNode | None = None
    parent: BstNode | None = None  # Added in order to delete a node easier

    def __iter__(self) -> Iterator[str]:
        """
        >>> list(Node(0))
        [0]
        >>> list(Node(0, Node(-1), Node(1), None))
        [-1, 0, 1]
        """
        yield from self.left or []
        yield self.value
        yield from self.right or []

    def __repr__(self) -> str:
        from pprint import pformat

        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)

    @property
    def is_right(self) -> bool:
        return bool(self.parent and self is self.parent.right)


@dataclass
class BinarySearchTree:
    root: BstNode | None = None

    def __bool__(self) -> bool:
        return bool(self.root)

    def __iter__(self) -> Iterator[str]:
        yield from self.root or []

    def __str__(self) -> str:
        return str(self.root)

    def __reassign_nodes(self, node: BstNode, new_children: BstNode | None) -> None:
        if new_children is not None:  # reset its kids
            new_children.parent = node.parent
        if node.parent is not None:  # reset its parent
            if node.is_right:  # If it is the right child
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def empty(self) -> bool:
        return not self.root

    def __insert(self, value) -> None:
        """
        Insert a new node in Binary Search Tree with value label
        """
        new_node = BstNode(value)  # create a new Node
        if self.empty():  # if Tree is empty
            self.root = new_node  # set its root
        else:  # Tree is not empty
            parent_node = self.root  # from root
            if parent_node is None:
                return
            while True:  # While we don't get to a leaf
                if value < parent_node.value:  # We go left
                    if parent_node.left is None:
                        parent_node.left = new_node  # We insert the new node in a leaf
                        break
                    else:
                        parent_node = parent_node.left
                elif parent_node.right is None:
                    parent_node.right = new_node
                    break
                else:
                    parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *values) -> Self:
        for value in values:
            self.__insert(value)
        return self

    def search(self, value) -> BstNode | None:
        if self.empty():
            raise IndexError("Warning: Tree is empty! please use another.")
        else:
            node = self.root
            # lazy evaluation, avoid NoneType Attribute error
            while node is not None and node.value is not value:
                node = node.left if value < node.value else node.right
            return node

    def get_max(self, node: BstNode | None = None) -> BstNode | None:
        if node is None:
            if self.root is None:
                return None
            node = self.root
        if not self.empty():
            while node.right is not None:
                node = node.right
        return node

    def get_min(self, node: BstNode | None = None) -> BstNode | None:
        if node is None:
            node = self.root
        if self.root is None:
            return None
        if not self.empty():
            node = self.root
            while node.left is not None:
                node = node.left
        return node

    def remove(self, value: int) -> None:
        node = self.search(value)
        if node is None:
            msg = f"Value {value} not found"
            raise ValueError(msg)

        if node.left is None and node.right is None:  # If it has no children
            self.__reassign_nodes(node, None)
        elif node.left is None:  # Has only right children
            self.__reassign_nodes(node, node.right)
        elif node.right is None:  # Has only left children
            self.__reassign_nodes(node, node.left)
        else:
            predecessor = self.get_max(
                node.left
            )  # Gets the max value of the left branch
            self.remove(predecessor.value)  # type: ignore[union-attr]
            node.value = (
                predecessor.value  # type: ignore[union-attr]
            )  # Assigns the value to the node to delete and keep tree structure

    def preorder_traverse(self, node: BstNode | None) -> Iterable:
        if node is not None:
            yield node  # Preorder Traversal
            yield from self.preorder_traverse(node.left)
            yield from self.preorder_traverse(node.right)

    def inorder_traverse(self, node: BstNode | None) -> Iterable:
        if node is not None:
            yield from self.inorder_traverse(node.left)
            yield node
            yield from self.inorder_traverse(node.right)

    def postorder_traverse(self, node: BstNode | None) -> Iterable:
        if node is not None:
            yield from self.postorder_traverse(node.left)
            yield from self.postorder_traverse(node.right)
            yield node

    def traversal_tree(self, traversal_function=None) -> Iterable:
        """
        This function traversal the tree.
        You can pass a function to traversal the tree as needed by client code
        """
        if traversal_function is None:
            return self.preorder_traverse(self.root)
        else:
            return traversal_function(self.root)


if __name__ == "__main__":
    # import doctest
    #
    # doctest.testmod(verbose=True)
    t = BinarySearchTree().insert(
        "e",
        "c",
        "g",
        "b",
        "d",
        "f",
        "h",
        "a",
        "i",
        "j",
    )
    print2D(t.root)

    print(tuple(i.value for i in t.traversal_tree()))

    # time_it(t.search, int(sys.argv[1]) if len(sys.argv) > 1 else 10)
    # print(t)
    # print(" ".join(repr(i) for i in t))

    #
    # print(tuple(i.value for i in t.traversal_tree(t.inorder_traverse)))
    # print(tuple(t))
    #
    # print(" ".join(repr(i.value) for i in t.traversal_tree(t.postorder_traverse)))
    # # t.remove(20)
    #
    # testlist = (8, 3, 6, 1, 10, 14, 13, 4, 7)
    # t = BinarySearchTree()
    # COUNT = [10]
    # for i in testlist:
    #     t.insert(i)  # doctest: +ELLIPSIS
    # print2DUtil(t.root)
