def solve(n, a, b):
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        a[i] -= min(a[i], b[i])
        b[i] -= min(a[i], b[i])
        ans += min(a[i+1], b[i])
        a[i+1] -= min(a[i+1], b[i])
        b[i] -= min(a[i+1], b[i])
    return ans
