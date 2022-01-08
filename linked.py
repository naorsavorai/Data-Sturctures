from node import Node


class Linked(object):
    head = None
    tail = None
    length = 0

    def __init__(self):
        self.head = None
        self.tail = self.head

    def __init__(self, intgr):
        self.length += 1
        self.head = Node(intgr)
        self.tail = self.head

    def print_list(self):
        cur_node = self.head
        while cur_node.get_next() is not None:
            print(cur_node.val, end=', ')
            cur_node = cur_node.get_next()
        print(f"{cur_node.val}")

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail
