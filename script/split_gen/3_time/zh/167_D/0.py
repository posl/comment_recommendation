def solve(n, k, a):
    k = k % n
    for i in range(k):
        a = a[a[i] - 1]
    return a
