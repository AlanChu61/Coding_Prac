"""
Tree in Python
"""


# class Node:
#     def __init__(self, data, children=None):
#         self.data = data
#         self.children = children  # []

#     def __repr__(self):
#         # Reader-friendly representation.

#         return f"<Node {self.data}>"


# # """Adding"""
# # rachna = Node('Ranchna')
# # taylor = Node('Taylor')

# # """rach is parent, taylor is children"""
# # rachna.children.append(taylor)

# # Finding a node


#     def find_DFS(self, data):
#         to_visit = [self]
#         while to_visit:
#             # BFS -> get the first of to_vist
#             # current = to_visit(0)
#             # DFS
#             current = to_visit.pop()
#             if current.data == data:
#                 return current
#             to_visit.extend(current.children)
#         pass

#     def find_BFS(self, data):
#         # BFS implemetation by using deque
#         from collections import deque
#         to_visit = deque[self]

#         while to_visit:
#             current = to_visit.popleft()
#             if current == data:
#                 return current
#             to_visit.extend(current.children)


# """
# BST
# """


# class BSTNode:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right

#     def __repr__(self):
#         return f"<BinaryNode {self.data}>"

#     def find(self, sought):
#         current = self

#         while current:
#             if current.data == sought:
#                 return current
#             elif current.data > sought:
#                 current = self.left
#             elif current.data < sought:
#                 current = self.right

"""
Whiteboarding 6: Trees
"""

"""
For all non-binary Tree problems below, assume any Node class to be defined as follows:"""


class Node:
    """Node in a tree."""

    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []


class BinarySearchNode:
    """Binary tree node."""

    def __init__(self, data, left=None, right=None):
        self.data = data

        self.left = left
        self.right = right


"""
Challenge1
Given a tree Node class, write a method that returns the number of nodes in the tree. (self is the root of the tree).
"""


def get_node_count_tree_DFS(self):
    count = 0
    to_visit = [self]

    while to_visit:
        count += 1
        current = to_visit.pop()
        to_visit.extend(current.children)
    return count


def get_node_count_tree_BFS(self):
    from collections import deque
    count = 0
    to_visit = deque()
    to_visit.append(self)
    while to_visit:
        current = to_visit.popleft()
        count += 1
        to_visit.extend(current.children)
    return count


"""
Challenge 2
Given a tree Node class, write a method that takes an item as its only parameter and returns True if the data for any node in the tree matches the given item. Otherwise, it should return False.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def find_item_DFS(self, value):
        to_visit = []
        to_visit.append(self)
        while to_visit:
            current = to_visit.pop()
            if current.data == value:
                return True
            to_visit.extend(current.children)
        return False

    def find_item_BFS(self, value):
        from collections import deque
        to_visit = deque()
        to_visit.append(self)

        while to_visit:
            current = to_visit.popleft()
            if current.data == value:
                return True
            to_visit.extend(current.children)
        return False


"""
Challenge 3
Given a tree Node class, write a method that takes an item as its only parameter and returns the highest ranking node whose data matches the given item. (If there are no matching nodes, it should return None).
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def find_rank(self, value):
        # use BFS
        from collections import deque
        to_visit = deque()
        to_visit.append(self)
        while to_visit:
            current = to_visit.popleft()
            if current.data == value:
                return current
            to_visit.extend(current.children)
        return False


"""
Challenge 4
Given a BinarySearchNode class, write a method that takes an item as its only parameter and returns the node in the BST whose data matches the given parameter. Be sure to discuss the runtime complexity of your solution.
"""


class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def find_BST(self, value):
        current = self

        while current:
            if current.data > value:
                current = current.left
            elif current.data < value:
                current = current.right
            elif current.data == value:
                return current
        return None
    # runtime logn

    def find_recursive(self, data_to_find):
        """Return node with this data. Return None if not found."""

        if self.data == data_to_find:
            return self
        elif data_to_find < self.data and self.left is not None:
            return self.left.find_recursive(data_to_find)
        elif data_to_find > self.data and self.right is not None:
            return self.right.find_recursive(data_to_find)
        else:
            return None


"""
Challenge 5
Given a tree Node class, write a method that takes an item and a node as its two parameters, and adds the new node as a child of the first node in the tree whose data matches the given item.

(You may assume that there are no nodes with duplicate data in the tree, or you may decide to define “first node” using breadth-first or depth-first search, or your interviewer may decide for you).
"""


def add_note_given_value(self, item, node):
    # DFS
    to_visit = [self]
    while to_visit:
        current = to_visit.pop()
        if current.data == item:
            current.children.append(node)
            return True
        to_visit.extend(current.children)
    return False


"""
Challenge 6
Given a BinarySearchNode class, write a method that returns the total number of nodes in the tree.
"""


def BST_count_node(self):
    # we can use DFS or BFS to approach
