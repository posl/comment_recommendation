def maximum_absolute_difference_of_two_elements(array):
    array.sort()
    return array[-1] - array[0]
