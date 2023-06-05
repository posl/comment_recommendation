def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1
