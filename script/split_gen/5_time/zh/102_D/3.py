def get_min_max_diff(array):
    n = len(array)
    if n < 4:
        return 0
    if n == 4:
        return min(array[3] - array[0], array[2] - array[1])
    if n == 5:
        return min(array[4] - array[0], array[3] - array[1], array[2] - array[2])
    if n == 6:
        return min(array[5] - array[0], array[4] - array[1], array[3] - array[2])
    if n == 7:
        return min(array[6] - array[0], array[5] - array[1], array[4] - array[2], array[3] - array[3])
    array.sort()
    return min(array[n-1] - array[0], array[n-2] - array[1], array[n-3] - array[2], array[n-4] - array[3])
