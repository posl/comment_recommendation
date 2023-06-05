def find_second_min(array):
    if array[0] < array[1]:
        min = array[0]
        second_min = array[1]
    else:
        min = array[1]
        second_min = array[0]
    for i in range(2, len(array)):
        if array[i] < min:
            second_min = min
            min = array[i]
        elif array[i] < second_min:
            second_min = array[i]
    return second_min
