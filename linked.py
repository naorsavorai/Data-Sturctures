from node import Node


class Linked(object):
    head = None
    tail = None
    length = 0

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __init__(self, intgr):
        self.length += 1
        self.head = Node(intgr)
        self.tail = self.head

    def print_list(self):
        cur_node = self.head
        if cur_node is None:
            print("Empty List")
            return
        while cur_node.get_next() is not None:
            print(cur_node.val, end=', ')
            cur_node = cur_node.get_next()
        print(f"{cur_node.val}")

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def get_length(self):
        return self.length

    def set_head(self, node):
        self.head = node

    def set_tail(self, node):
        self.tail = node
