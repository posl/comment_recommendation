def solve(n, a):
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += a[i] * 2
    ans += a[-1]
    return ans
