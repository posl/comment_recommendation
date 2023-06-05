def solve(n, k, x, a):
    a.sort()
    ans = 0
    for i in range(n):
        if k > 0:
            ans += max(a[i] - x, 0)
            k -= 1
        else:
            ans += a[i]
    return ans
