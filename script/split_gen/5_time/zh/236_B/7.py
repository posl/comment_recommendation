def problem236_b(n, a):
    a.sort()
    for i in range(0, 4*n-1, 2):
        if a[i] != a[i+1]:
            return a[i]
    return a[-1]
