from array import *


def create_an_array():
    return array("i", [10, 20, 30, 40, 50])


def print_array(arr):
    for x in arr:
        print(x)


def example1_create_and_print():
    print_array(create_an_array())


def example2_access_an_element():
    arr = create_an_array()
    print(arr[0])
    print(arr[2])


def example3_insert_an_element():
    arr = create_an_array()
    arr.insert(1, 60)
    print_array(arr)


def example4_remove_an_element_with_value():
    arr = create_an_array()
    arr.remove(40)
    print_array(arr)


def example5_remove_an_element_with_duplicates():
    arr = array("i", [10, 20, 30, 20, 40, 50])
    arr.remove(20)
    print_array(arr)


def example6_delete_an_element_with_index():
    # say element at index 3 is not supposed to be there
    # delete it with the index
    arr = array("i", [10, 20, 30, 20, 40, 50])
    del arr[3]
    print_array(arr)


def example7_search_for_an_element_with_value():
    arr = create_an_array()
    print(arr.index(40))


def example8_search_for_an_element_with_duplicates():
    # when there is duplicates in the array, it only returns the first match
    arr = array("i", [10, 20, 30, 40, 20, 50])
    print(arr.index(20))


def example9_update_value_of_element():
    arr = create_an_array()
    arr[2] = 80
    print_array(arr)
