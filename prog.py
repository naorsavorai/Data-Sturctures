from heap import HeapA, HeapB


def get_command(inp, i):
    command = ""
    if (inp == ""):
        return command
    while i < len(inp) and user_input[i] == " ":
        i += 1
        if i >= len(inp):
            break
    while ("a" <= user_input[i] <= "z") or ("A" <= user_input[i] <= "Z"):
        command += user_input[i]
        i += 1
        if i >= len(inp):
            break

    return command


def user_input_parser(command, user_input, dic, flag):
    if command == "BuildHeap" or command == "buildheap":
        use_make_heap(user_input, dic, flag)
        return
    if command == "Insert" or command == "insert":
        use_insert(user_input, dic)
        return
    if command == "Union" or command == "union":
        use_merge(user_input, dic)
        return
    if command == "ExtractMin" or command == "extractmin":
        use_extract_min(user_input, dic)
        return
    if command == "GetMin" or command == "getmin":
        use_get_minimum(user_input, dic)
        return
    if command == "PrintHeap" or command == "printheap":
        use_print_heap(user_input, dic)
        return
    else:
        print("Invalid Command")


def use_merge(inp, dic):
    aux = inp.split(" ")
    if len(aux) < 3:
        print("Invalid input: Please enter two heap names ")

    else:
        heap1_name = aux[1]
        heap2_name = aux[2]
        heap1 = dic.get(heap1_name)
        heap2 = dic.get(heap2_name)
        if heap1 is None or heap2 is None:
            print("Couldn't find one of requested heaps")
        else:
            res = heap1.merge(heap2)
            res_name = f"{heap1_name}#{heap2_name}"
            dic[res_name] = res
            print(f"Merged heap {heap2_name} and {heap1_name} into heap {res_name}")


def use_get_minimum(inp, dic):
    aux = inp.split(" ")
    len(aux)
    if len(aux) < 2:
        print("Invalid input: Please enter a heap name ")
    else:
        heaps_name = aux[1]
        heap = dic.get(heaps_name)
        if heap is None:
            print("Couldn't find the requested heap")
        else:
            res = heap.get_minimum()
            print(f"Minimum of heap {heaps_name} is {res}")


def use_extract_min(inp, dic):
    aux = inp.split(" ")
    if len(aux) < 2:
        print("Invalid input: Please enter a heap name ")
    else:
        heaps_name = aux[1]
        heap = dic.get(heaps_name)
        if heap is None:
            print("Couldn't find the requested heap")
        else:
            res = heap.extract_min()
            print(f"Extracted minimum of heap {res} from heap {heaps_name}")


def use_make_heap(inp, dic, flag):
    aux = inp.split(" ")
    if len(aux) < 2:
        print("Invalid input: Please enter a heap name ")
    else:
        heaps_name = aux[1]
        if flag == "unsorted":
            new_heap = HeapA()
        else:
            new_heap = HeapB()
        dic[f"{heaps_name}"] = new_heap
        print(f"Made heap: {heaps_name}")


def use_insert(inp, dic):
    aux = inp.split(" ")
    if len(aux) < 2:
        print("Invalid input: Please enter a heap name and at least one integer")
        return
    else:
        heaps_name = aux[1]
        heap = dic.get(heaps_name)
        if heap is None:
            print("Couldn't find the requested heap")
        else:
            for index in range(2, len(aux)):
                try:
                    value = int(aux[index])
                    heap.insert(value)
                    print(f"Inserted {value} to heap {heaps_name}")
                except ValueError:
                    continue


def use_print_heap(inp, dic):
    aux = inp.split(" ")
    if len(aux) < 2:
        print("Invalid input: Please enter a heap name ")
    else:
        heap_name = aux[1]
        heap = dic.get(heap_name)
        if heap is None:
            print("Couldn't find the requested heap")
        else:
            heap.print_list()


"""********************************************************* Main program *************************************************************************************************** """
heaps = {}
num = 0
while True:
    try:
        flag = input("Please enter \"sorted\" for sorted lists or \"unsorted\" for unsorted lists:")
        if flag != "sorted" and flag != "unsorted" and flag != "stop":
            print("Not a flag")
            raise RuntimeWarning("Wrong Flag")
        break
    except RuntimeWarning:
        continue
if flag != "stop":
    print(f"Flag confirmed, using {flag} data structures, please enter your commands:")
else:
    print("flag \"stop\" is confirmed exiting program")
while True:
    if flag == "stop":
        break
    i = 0
    try:
        user_input = input()
    except EOFError:
        print("Good Bye")
        break
    command = get_command(user_input, i)
    if user_input == "":
        continue
    if command == 'stop' or command == 'Stop':
        print("Good Bye ")
        break
    user_input_parser(command, user_input, heaps, flag)
