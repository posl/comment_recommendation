def solve(n, k, h):
    h.sort()
    ans = 10 ** 9
    for i in range(n - k + 1):
        ans = min(ans, h[i + k - 1] - h[i])
    return ans
