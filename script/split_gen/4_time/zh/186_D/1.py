def solve(n, a):
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (i * 2 - n + 1)
    return ans
