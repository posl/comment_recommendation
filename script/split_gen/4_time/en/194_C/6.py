def solve(n, a):
    ans = 0
    for i in range(n):
        ans += a[i] * a[i] * (n - 1)
    for i in range(n - 1):
        ans -= 2 * a[i] * sum(a[i + 1:])
    return ans
