def binary_search(array, value):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == value:
            return middle
        elif array[middle] < value:
            left = middle + 1
        else:
            right = middle - 1
    return left
