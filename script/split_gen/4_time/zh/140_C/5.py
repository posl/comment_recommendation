def max_sum(n, b):
    a = [0 for i in range(n)]
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(1, n-1):
        if b[i] <= b[i-1]:
            a[i] = b[i]
        else:
            a[i] = b[i-1]
    return sum(a)
