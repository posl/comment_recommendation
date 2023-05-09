def median(n, a):
    a.sort()
    if n % 2 == 1:
        return a[n // 2]
    else:
        return a[(n - 1) // 2]
