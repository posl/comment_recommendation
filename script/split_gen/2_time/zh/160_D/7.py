def solve(k, n, a):
    ans = k
    for i in range(n - 1):
        ans = min(ans, k - abs(a[i + 1] - a[i]))
    return ans
