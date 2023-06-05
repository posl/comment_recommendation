def solve(n, d, x, y):
    ans = 0
    for i in range(n):
        if x[i] ** 2 + y[i] ** 2 <= d ** 2:
            ans += 1
    return ans
