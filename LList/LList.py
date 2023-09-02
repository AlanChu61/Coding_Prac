"""The Node Class"""


class Node:
    """Node in a LL"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        # 当你使用str()函数或内置的print()函数来表示一个对象时，
        return str(self.data)

    def __repr__(self):
        # 直接在交互式解释器中输入对象名称
        return f"<Node Obj. Data:{self}; Next:{self.next}>"


class LinkedList:
    def __init__(self):
        self.head = None

    # Traversing
    def print_list(self):
        current = self.head
        while current:
            print(current)
            current = current.next
    # Searching

    def find(self, data):
        current = self.head
        while current:
            if current == data:
                return True
            current = current.next
        return False

    # Appending/Removing Nodes¶
    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        if self.tail:
            self.tail.next = new_node

        self.tail = new_node

    def remove_by_value(self, data):
        # if head.data == data, remove head
        if self.head and self.head.next == data:
            self.head = self.head.next
            if not self.head:
                # it indicates that self.head == none(it was only one node in the LL)
                # None LList
                # self.tail == None
                self.tail = None
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                if not current.next:
                    self.tail = None
                    return
            else:
                current = current.next


my_list = LinkedList()
