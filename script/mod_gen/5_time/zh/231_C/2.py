def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right

if __name__ == '__main__':
    binary_search()