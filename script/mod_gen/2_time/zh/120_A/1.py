def find_nearest(array, item):
    if item < array[0]:
        return array[0]
    if item > array[-1]:
        return array[-1]
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == item:
            return array[mid]
        elif array[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    if abs(array[low] - item) < abs(array[high] - item):
        return array[low]
    else:
        return array[high]

if __name__ == '__main__':
    find_nearest()