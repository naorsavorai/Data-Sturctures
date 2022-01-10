from linked import Linked
from node import Node
import math


def swap(node1, node2):
    tmp = node1.get_val()
    node1.set_val(node2.get_val())
    node2.set_val(tmp)


def get_parent(node, index):
    res = node
    for i in range(index - math.floor(index / 2)):
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
    if parent is None or parent.get_val() < node.get_val():
        return
    else:
        swap(node, parent)
        par_index = math.floor(index / 2)
        heapify(parent, par_index)


class HeapA(Linked):

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def initiate(self, heap):
        cur_node = heap.get_head()
        while cur_node is not None:
            self.insert(cur_node.get_val())
            cur_node = cur_node.get_next()

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
        res = HeapA()
        res.initiate(self)
        cur = heap2.get_head()
        while cur is not None:
            res.insert(cur.get_val())
            cur = cur.get_next()
        return res


class HeapB(Linked):

    def __init__(self):
        self.length = 0
        self.tail = None
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        elif val < self.get_tail().get_val():
            print("Error: Input must be sorted ")
        else:
            prev_node = self.head
            if prev_node.get_val() >= val:
                new_node.set_next(prev_node)
                prev_node.set_prev(new_node)
                self.head = new_node
                return
            next_node = self.head.get_next()
            while next_node is not None:
                if prev_node.get_val() <= val < next_node.get_val():
                    new_node.set_next(next_node)
                    new_node.set_prev(prev_node)
                    prev_node.set_next(new_node)
                    next_node.set_prev(new_node)
                    return
                prev_node = prev_node.get_next()
                next_node = next_node.get_next()
            new_node.set_prev(prev_node)
            prev_node.set_next(new_node)

    def get_minimum(self):
        minimum = self.get_head().get_val()
        return minimum

    def extract_min(self):
        res = self.get_minimum()
        new_head = self.get_head().get_next()
        old_head = self.get_head()
        new_head.set_prev(None)
        old_head.set_next(None)
        self.head = new_head
        return res

    def merge(self, sorted_list):
        res = HeapB()
        a_node = self.get_head()
        b_node = sorted_list.get_head()
        if a_node.get_val() <= b_node.get_val():
            cur_node = Node(a_node.get_val())
            a_node = a_node.get_next()
        else:
            cur_node = Node(b_node.get_val())
            b_node = b_node.get_next()
        res.set_head(cur_node)
        while a_node is not None and b_node is not None:
            if a_node.get_val() <= b_node.get_val():
                cur_node.set_next(Node(a_node.get_val()))
                a_node = a_node.get_next()
            else:
                cur_node.set_next(Node(b_node.get_val()))
                b_node = b_node.get_next()
            cur_node = cur_node.get_next()

        if a_node is None and b_node is not None:
            while b_node is not None:
                cur_node.set_next(Node(b_node.get_val()))
                b_node = b_node.get_next()
                cur_node = cur_node.get_next()

        if b_node is None and a_node is not None:
            while a_node is not None:
                cur_node.set_next(Node(a_node.get_val()))
                a_node = a_node.get_next()
                cur_node = cur_node.get_next()
        res.set_tail(cur_node)
        return res
