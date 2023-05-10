def binary_search(array, num):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == num:
            return mid
        elif array[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return left

if __name__ == '__main__':
    binary_search()