def cuberoot(x):
    l = 1
    r = x
    while l < r:
        mid = (l + r) // 2
        if mid ** 3 < x:
            l = mid + 1
        else:
            r = mid
    return l
