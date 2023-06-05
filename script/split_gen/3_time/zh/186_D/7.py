def solve(n, a):
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2 * i - n + 1)
    return ans
