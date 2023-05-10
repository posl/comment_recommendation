def swap(n, x):
    for i in range(1, n):
        if x[i-1] > x[i]:
            x[i-1], x[i] = x[i], x[i-1]
    return x
