#!/usr/bin/env python
"""
    Input Format. The first line contains the number of nodes 𝑛. The second line contains 𝑛 integer numbers
    from −1 to 𝑛 − 1 — parents of nodes. If the 𝑖-th one of them (0 ≤ 𝑖 ≤ 𝑛 − 1) is −1, node 𝑖 is the root,
    otherwise it’s 0-based index of the parent of 𝑖-th node. It is guaranteed that there is exactly one root.
    It is guaranteed that the input represents a tree.
    
    Example input:
    5
    4 -1 4 1 1
"""
import argparse
from queue import Queue

parser = argparse.ArgumentParser()
parser.add_argument("--nodes", help="Number of nodes in the Tree", type=int)
parser.add_argument("--parents", help="The list of parents separated by white spaces")

args = parser.parse_args()

class Tree:
    key: any
    child_trees: list
    
    def __init__(self, key = None, child_trees = []) -> None:
        self.key = key
        self.child_trees = child_trees
        
    # def __str__(self) -> str:
    #     childs = self.child_trees
    #     has_next_level = redu
    #     while childs in self.child_trees:
    #         " ".join(str(child))
    #     op 
        
    def has_child(self):
        return self.child_trees is not None
        
    def is_empty(self):
        return self.key is None and not self.child_trees
    
    def add_node(self, node):
        if self.child_trees:
            self.child_trees.append(node)
        else:
            self.child_trees = [node]
    
    def set_key(self, key):
        self.key = key
    
    def height(self):
        if self.is_empty():
            return 0
        elif self.key is not None and not self.child_trees:
            return 1
        else:
            return max([node.height() for node in self.child_trees]) + 1
    
    def pre_order_traversal(self, func):
        """
        apply func to every key in the tree, traversing all elements in a branch before moving to the next
        """
        if self.is_empty():
            return
        func(self.key)
        for child_tree in self.child_trees:
            child_tree.pre_order_traversal(func)
            
    def post_order_traversal(self, func):
        """
        apply func to every key in the tree, traversing all elements in a branch before moving to the next
        """
        if self.is_empty():
            return
        for child_tree in self.child_trees:
            child_tree.post_order_traversal(func)
        func(self.key)
            
    def level_traversal(self, func):
        """
        apply func to every key in the tree, traversing all elements in a level before moving to the next
        """
        if self.is_empty():
            return
        pending_queue = Queue()
        pending_queue.put(self)
        while not pending_queue.empty():
            node = pending_queue.get()
            func(node)
            for child in node.child_trees:
                pending_queue.put(child)
        
class TreeFactory:
    def __init__(self, nodes, parents) -> None:
        self.nodes = nodes
        self.parents = parents
        self.tree_map = dict()
    
    def build(self) -> Tree:
        parent_list: list = [int(x) for x in self.parents.split(" ")]
        for key in range(self.nodes):
            self.tree_map.update({
                key: Tree(key)
            })
        for index, key in enumerate(parent_list):
            tree: Tree = self.tree_map.get(index, None)
            parent_tree: Tree = self.tree_map.get(key, None)
            if parent_tree:
                parent_tree.add_node(tree)
        root = parent_list.index(-1)
        return self.tree_map.get(root, None)
        
factory = TreeFactory(args.nodes, args.parents)
tree = factory.build()
tree.level_traversal(lambda x: print(x.height()))