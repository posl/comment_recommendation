def main():
    N, K = map(int, input().split())
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(i+1):
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
            dp[i][j] += dp[i-1][j] * (i-j)
            dp[i][j] %= 10**9+7
    for i in range(1, K+1):
        print(dp[N][i])
main()
