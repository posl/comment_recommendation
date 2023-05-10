def main():
    n = int(input())
    mod = 998244353
    dp = [[0 for _ in range(10)] for _ in range(n)]
    dp[0][0] = 0
    for i in range(1, 10):
        dp[0][i] = 1
    for i in range(1, n):
        dp[i][0] = dp[i - 1][1]
        for j in range(1, 9):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod
        dp[i][9] = dp[i - 1][8]
    ans = 0
    for i in range(10):
        ans += dp[n - 1][i]
        ans %= mod
    print(ans)
