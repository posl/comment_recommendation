def maxsum(n, b):
    a = [0 for i in range(n)]
    a[0] = b[0]
    for i in range(1, n-1):
        a[i] = max(b[i], b[i-1])
    a[-1] = b[-1]
    return sum(a)
