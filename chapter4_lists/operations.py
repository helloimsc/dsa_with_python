def get_mix_list():
    return ["physics", "chemistry", 1997, 2000]


def get_num_list():
    return [1, 2, 3, 4, 5, 6, 7]


def example1_accessing_values():
    list1 = get_mix_list()
    list2 = get_num_list()
    print("list1[0]: ", list1[0])
    print("list2[1:5]: ", list2[1:5])


def example2_updating_value():
    list = get_mix_list()
    print("Value available at index 2: ", list[2])
    list[2] = 2001
    print("New value available at index 2: ", list[2])


def example3_delete_element():
    list1 = get_mix_list()
    print(list1)
    del list1[2]
    print("After deleting value at index 2: ", list1)
