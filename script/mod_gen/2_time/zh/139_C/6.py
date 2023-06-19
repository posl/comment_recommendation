def solve(n, h):
    dp = [0] * n
    dp[0] = 0
    dp[1] = 1 if h[0] >= h[1] else 0
    for i in range(2, n):
        if h[i-1] >= h[i]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 0
    return max(dp)
n = int(input())
h = list(map(int, input().split()))
print(solve(n, h))
