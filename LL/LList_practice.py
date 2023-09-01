
"""
resources:
https://fellowship.hackbrightacademy.com/materials/serft21/lectures/linkedlists/
https://fellowship.hackbrightacademy.com/materials/serft21/exercises/whiteboarding-5/
https://fellowship.hackbrightacademy.com/materials/serft21/exercises/whiteboarding-5/solution/
"""


"""
Define a Queue class and implement the following methods: __init__, enqueue, dequeue, and is_empty. Specify the runtime of all methods except __init__.
"""

# Queue Class




from collections import deque
class Queue:
    def __init__(self):
        # self.data = []
        self.data = deque

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        # return the poped out item
        if self.is_empty():
            return None
        # return self.data.pop(0)
        return self.data.popleft()

    def is_empty(self):
        return len(self.data) == 0

# Linked List Node/Traversal¶


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head == None:
            print("It is an emp LL")
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next


"""
Here is a snippet from a linked list class:

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
Write a method called print_odd_nodes that prints the nodes with odd-numbered indices (1, 3, 5, …, etc.)
"""


def print_odd_nodes(self):
    if self.head is None:
        print('empty LL')
        # 要把self.head 想像就是一個箭頭
    current = self.head
    index = 1
    while current:
        if index % 2 != 0:
            print(current.data)
        current = current.next
        index += 1


"""
Here’s a snippet from a linked list class:

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
Write a method for this class called append. It should take in a node instance and add it to the end of the linked list.
"""


def append(self, node):
    if self.head is None:
        self.head = node
        self.tail = node
        return
    self.tail.next = node
    self.tail = node


"""
Write a function that removes a node with a given value from a singly-linked list. It should return the head node. The function should take in two arguments:

head — the head of a linked list

value — a value that you want to remove
"""


def remove_by_val(head, value):
    if head is None:
        print('empty LL')
        return head
    if head.data == value:
        return head.next

    current = head.next
    while current:
        if current.data == value:
            current.next = current.next.next
            return head
        current = current.next
    return head


"""
Here’s a snippet from a doubly-linked list class:

class DblLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
Write a method for this class called remove. It should take in a node instance and remove it from the list.
"""


def remove(self, node):
    if node is None:
        return
    if node.prev is None:
        # head
        self.head = node.next
    else:
        """
        当从双向链表中移除一个节点时，需要确保链表的前一个节点和后一个节点正确地连接起来，以保持链表的连续性。在双向链表中，每个节点都有一个指向前一个节点的指针 prev 和一个指向后一个节点的指针 next。

        假设我们有以下的双向链表，其中每个节点都用数字表示：
        1 <-> 2 <-> 3 <-> 4
        现在，假设我们要移除节点 2。我们可以使用 node.next.prev = node.prev 来更新指向节点 3 的 prev 指针，以使其指向节点 1，如下所示：


        1 <-> 3 <-> 4
        这意味着我们将节点 2 从链表中移除，并且节点 3 的 prev 指针现在指向了节点 1，以保持链表的连续性。在双向链表中，这种操作允许我们同时访问前一个节点和后一个节点，从而有效地移除当前节点。

        当你执行 node.next.prev = node.prev 这句代码时，你实际上是在更新节点 3 的 prev 指针，让它指向节点 1。这样，节点 2 就从链表中被成功移除了。这是双向链表中常用的操作，以确保链表的正确性。
        """
        node.prev.next = node.next
    if node.next is None:
        self.tail = node.prev
    else:
        node.next.prev = node.next


"""
Write a function that takes in the head of a singly-linked list. It should return True if two nodes with the same data appear consecutively.

Example test cases:

in: 1 → 2 → 2
out: True
"""


def remove(head):
    if head is None:
        return False
    current = head
    while current.next:
        if current.data == current.next.data:
            return True
        current = current.next

    return False
