def solve(n, a):
    s = 0
    for i in range(1, n):
        for j in range(i):
            s += (a[i] - a[j]) ** 2
    return s
