def solve(n, k, h):
    h.sort()
    ans = 0
    for i in range(n - k):
        ans += h[i]
    return ans
