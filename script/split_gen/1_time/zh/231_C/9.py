def binary_search(a, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a, x, low, mid - 1)
    else:
        return binary_search(a, x, mid + 1, high)
