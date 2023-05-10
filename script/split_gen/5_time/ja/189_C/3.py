def max_orange(n, a):
    ans = 0
    for l in range(n):
        min_orange = a[l]
        for r in range(l, n):
            min_orange = min(min_orange, a[r])
            ans = max(ans, min_orange * (r - l + 1))
    return ans
