def solve(n, m, a):
    if n < sum(a):
        return -1
    return n - sum(a)
