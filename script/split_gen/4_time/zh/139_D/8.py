def solve(n):
    n = int(n)
    res = 0
    for i in range(1, n + 1):
        res += n // i * i
    return res
