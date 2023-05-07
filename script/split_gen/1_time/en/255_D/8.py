def solve(n, q, a, x):
    a.sort()
    x.sort()
    ans = 0
    for i in range(q):
        ans += (x[i] - a[i]) if x[i] > a[i] else (a[i] - x[i])
    return ans
