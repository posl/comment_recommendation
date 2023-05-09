def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    MOD = 998244353
    dp = [[0 for i in xrange(3001)] for j in xrange(3001)]
    dp[0][0] = 1
    for i in xrange(n):
        for j in xrange(a[i], b[i] + 1):
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
            dp[i + 1][j] = (dp[i + 1][j] + dp[i + 1][j - 1]) % MOD
    print dp[n][b[n - 1]]
