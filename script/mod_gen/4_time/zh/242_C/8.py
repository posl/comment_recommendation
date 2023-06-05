def solve(n):
    mod = 998244353
    dp = [[0 for _ in range(10)] for _ in range(n+1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(0, 10):
            for k in range(0, 10):
                if abs(j-k) <= 1:
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %= mod
    ans = 0
    for i in range(0, 10):
        ans += dp[n][i]
        ans %= mod
    return ans

if __name__ == '__main__':
    solve()