def f(x, m):
    d = max(map(int, x))
    l = d + 1
    r = m + 1
    while l < r:
        mid = (l + r) // 2
        if int(x, mid) <= m:
            l = mid + 1
        else:
            r = mid
    return l - d - 1
