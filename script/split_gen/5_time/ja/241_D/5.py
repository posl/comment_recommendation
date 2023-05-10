def binary_search(a, x):
    l = 0
    r = len(a) - 1
    while r - l >= 0:
        m = (l + r) // 2
        if a[m] == x:
            return m
        elif a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return l
