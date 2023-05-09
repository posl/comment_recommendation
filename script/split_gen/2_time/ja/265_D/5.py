def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * 4 for _ in range(n + 1)]
    for i in range(n):
        dp[i + 1][0] = max(dp[i][0], a[i])
        dp[i + 1][1] = max(dp[i][1], dp[i + 1][0] + a[i])
        dp[i + 1][2] = max(dp[i][2], dp[i + 1][1] + a[i])
        dp[i + 1][3] = max(dp[i][3], dp[i + 1][2] + a[i])
    ans = 0
    for i in range(n):
        ans = max(ans, dp[i][0] * p + dp[i][1] * q + dp[i][2] * r + dp[i][3])
    print(ans)
