""" Task 6
Author: Andrii Malchyk
v.1.0
"""


def IsSorted(array, sort_order="ASC"):
    ''' The function takes two parameters: a sorted list of integer and sort order (ASC or DESC)
    '''
    if isinstance(array, list) and isinstance(sort_order, str):
        if (array[0] < array[1]) and (sort_order == "ASC"):
            return True
        elif (array[0] > array[1]) and (sort_order == "ASC"):
            return False
        elif (array[0] > array[1]) and (sort_order == "DESC"):
            return True
        elif (array[0] < array[1]) and (sort_order == "DESC"):
            return False
        else:
            print("Unexpected error!")
    else:
        print("Input parameters error!")
