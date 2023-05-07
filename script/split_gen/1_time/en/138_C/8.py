def main():
    n = int(input())
    v = list(map(int, input().split()))
    # dp[i][j] = i番目までの数字を使って、j個の数字を作ったときの最大値
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i][1] = v[i]
    for i in range(2, n+1):
        for j in range(1, n+1):
            for k in range(j):
                dp[i][j] = max(dp[i][j], (dp[i-1][k] + dp[i-1][j-k]) / 2)
    print(dp[n][n])
