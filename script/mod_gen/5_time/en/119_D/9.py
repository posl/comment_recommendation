def get_nearest(array, value):
    if value <= array[0]:
        return array[0]
    if value >= array[-1]:
        return array[-1]
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == value:
            return array[mid]
        elif array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return array[high] if abs(array[high] - value) < abs(array[low] - value) else array[low]

if __name__ == '__main__':
    get_nearest()