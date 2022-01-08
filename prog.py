from linked import Linked
from heap import HeapA
from node import Node


min_heap = HeapA()
min_heap2 = HeapA()


for _ in [4, 5, 2, 3,1, 20,-1]:
    min_heap.insert(_)
min_heap.print_list()
min_heap.extract_min()
print(min_heap.tail.get_val())
min_heap.print_list()

min_heap.insert(99)
min_heap.print_list()
min_heap.insert(-156)
min_heap.print_list()
min_heap.insert(77)
min_heap.print_list()
min_heap.insert(16)
min_heap.print_list()
min_heap.insert(0)
min_heap.print_list()
