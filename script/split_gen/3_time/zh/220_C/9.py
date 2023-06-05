def func(n, a, x):
    mod = 1000000007
    b = a * 100
    l = len(b)
    sum = 0
    for i in range(l):
        sum += b[i]
        if sum > x:
            return i + 1
    return -1
