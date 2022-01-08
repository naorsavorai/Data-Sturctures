class Node(object):
    val = 0
    next_n = None

    def __init__(self, x):
        self.val = x
        self.next_n = None

    def get_next(self):
        return self.next_n

    def get_val(self):
        return self.val

    def set_next(self, new_next):
        self.next_n = new_next

    def set_val(self, new_val):
        self.val = new_val

    def get_n_next(self, n):
        res = self
        for i in range(n):
            res = res.get_next()
        return res


class DoubleNode(Node):
    prev_n = None

    def __init__(self, value):
        self.val = value
        self.next_n = None
        self.prev_n = None

    def get_prev(self):
        return self.prev_n

    def set_prev(self, new_prev):
        self.prev_n = new_prev

    def get_n_prev(self, n):
        res = self
        for i in range(n):
            res = res.get_prev()
        return res
