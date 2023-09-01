"""
Tree in Python
"""


class Node:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children  # []

    def __repr__(self):
        # Reader-friendly representation.

        return f"<Node {self.data}>"


# """Adding"""
# rachna = Node('Ranchna')
# taylor = Node('Taylor')

# """rach is parent, taylor is children"""
# rachna.children.append(taylor)

# Finding a node

    def find_DFS(self, data):
        to_visit = [self]
        while to_visit:
            # BFS -> get the first of to_vist
            # current = to_visit(0)
            # DFS
            current = to_visit.pop()
            if current.data == data:
                return current
            to_visit.extend(current.children)
        pass

    def find_BFS(self, data):
        # BFS implemetation by using deque
        from collections import deque
        to_visit = deque[self]

        while to_visit:
            current = to_visit.popleft()
            if current == data:
                return current
            to_visit.extend(current.children)


"""
BST
"""


class BST:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<BinaryNode {self.data}>"
