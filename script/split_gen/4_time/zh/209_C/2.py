def solve(n, c):
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(c[i] - i, 0)
        ans %= 1000000007
    return ans
