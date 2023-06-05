def solve(n, m, a):
    a.sort()
    if a[0] == 0 and a[-1] == m - 1:
        return 0
    if a[0] == 0:
        return m - a[-1] - 1
    if a[-1] == m - 1:
        return a[0] - 1
    ans = 0
    for i in range(1, n):
        if a[i] == a[i - 1]:
            continue
        ans += a[i] - a[i - 1] - 1
    return ans
