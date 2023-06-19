def main():
    N = int(input())
    mod = 998244353
    dp = [[0] * 10 for _ in range(N)]
    for i in range(1, 10):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod
            elif j == 9:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
            else:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
                dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod
    print(sum(dp[-1]) % mod)
main()
