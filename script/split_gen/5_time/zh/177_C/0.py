def solve(n, a):
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(n):
        ans += a[i] * sum(a[i + 1:])
        ans %= mod
    return ans
