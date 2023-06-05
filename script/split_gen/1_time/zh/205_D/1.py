def binary_search(n, a, key):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if key == a[mid]:
            return mid
        elif key > a[mid]:
            left = mid + 1
        else:
            right = mid
    return -1
