from linked import Linked
from node import Node
import math


def swap(node1, node2):
    tmp = node1.get_val()
    node1.set_val(node2.get_val())
    node2.set_val(tmp)


def get_parent(node, index):
    res = node
    for i in range(0,index - math.floor(index / 2)):
        res = res.get_prev()
    return res


def get_left_son(node, index):
    res = node
    for i in range(index * 2 + 1):
        if res is None:
            break
        res = res.get_next()
    return res


def reverse_heapify(node, index):
    left_son = get_left_son(node, index)
    if left_son is None:
        return
    right_son = left_son.get_next()
    if right_son is None or left_son.get_val() <= right_son.get_val():
        if node.get_val() <= left_son.get_val():
            return
        swap(left_son, node)
        reverse_heapify(left_son, index * 2)
    else:
        if node.get_val() <= right_son.get_val():
            return
        swap(right_son, node)
        reverse_heapify(right_son, index * 2 + 1)


def heapify(node, index):
    parent = get_parent(node, index)
    if parent is None or parent.get_val() <= node.get_val():
        return
    else:
        swap(node, parent)
        par_index = math.floor(index / 2)
        heapify(parent, par_index)


class HeapA(Linked):
    def __init__(self):
        self.length = 0
        self.tail = None
        self.head = None

    def insert(self, x):
        new_node = Node(x)
        self.length += 1
        if self.tail is None:
            self.tail = new_node
            self.head = self.tail
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = self.tail.get_next()
            heapify(self.tail, self.length)

    def get_minimum(self):
        minimum = self.head.get_val()
        return minimum

    def remove_last(self):
        self.length -= 1
        self.tail = self.tail.get_prev()
        self.tail.set_next(None)

    def extract_min(self):
        minimum = self.head.get_val()
        swap(self.head, self.tail)
        self.remove_last()
        reverse_heapify(self.head, 0)
        return minimum

    def merge(self, heap2):
        cur = heap2.get_head()
        while cur is not None:
            self.insert(cur.get_val())
            cur = cur.get_next()
