def solve(n, m, a):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in a:
            if i - j >= 0:
                dp[i] = max(dp[i], dp[i - j] * 10 + j)
    return dp[n]
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))
