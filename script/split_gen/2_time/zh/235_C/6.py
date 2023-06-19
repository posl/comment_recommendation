def binary_search(a, x, k):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            if mid == 0 or a[mid - 1] != x:
                return mid + 1
            else:
                high = mid - 1
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
