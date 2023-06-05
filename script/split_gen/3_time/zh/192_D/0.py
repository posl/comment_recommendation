def solve(x, m):
    d = int(max(x))
    ans = 0
    for i in range(d + 1, 10):
        base = int(x, i)
        if base <= m:
            ans += 1
    return ans
