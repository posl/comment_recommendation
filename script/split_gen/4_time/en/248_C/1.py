def main():
    n, m, k = map(int, input().split())
    mod = 998244353
    dp = [[0 for i in range(k+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(k+1):
            dp[i][j] = dp[i-1][j] * m % mod
            if j > 0:
                dp[i][j] += dp[i-1][j-1] * (m-1) % mod
            dp[i][j] %= mod
    print(dp[n][k])
