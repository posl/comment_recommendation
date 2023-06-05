def main():
    n = int(input())
    mod = 998244353
    dp = [[0 for i in range(10)] for j in range(n)]
    for i in range(1,10):
        dp[0][i] = 1
    for i in range(n - 1):
        for j in range(10):
            if j == 0:
                dp[i + 1][j] = (dp[i][j] + dp[i][j + 1]) % mod
            elif j == 9:
                dp[i + 1][j] = (dp[i][j - 1] + dp[i][j]) % mod
            else:
                dp[i + 1][j] = (dp[i][j - 1] + dp[i][j] + dp[i][j + 1]) % mod
    ans = 0
    for i in range(10):
        ans += dp[n - 1][i]
        ans %= mod
    print(ans)
main()
