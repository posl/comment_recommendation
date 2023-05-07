def binary_search(arr, val):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == val:
            return m
        elif arr[m] > val:
            r = m - 1
        else:
            l = m + 1
    return l

if __name__ == '__main__':
    binary_search()