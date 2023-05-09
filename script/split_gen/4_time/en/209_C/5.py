def solve(n, c):
    mod = 10**9+7
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(0, c[i]-i)
        ans %= mod
    return ans
