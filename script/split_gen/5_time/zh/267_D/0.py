def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i][j] + a[i] * (j + 1), dp[i][j + 1])
    print(dp[n][m])
