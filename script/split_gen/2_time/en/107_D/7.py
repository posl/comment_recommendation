def solve(N, a):
    a.sort()
    ans = 0
    for i in range(N):
        ans += a[i] * (i * 2 - N + 1)
    return ans
