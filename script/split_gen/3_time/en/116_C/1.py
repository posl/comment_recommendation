def solve(N, h):
    ans = 0
    for i in range(N - 1):
        if h[i] > h[i + 1]:
            ans += h[i] - h[i + 1]
    return ans
