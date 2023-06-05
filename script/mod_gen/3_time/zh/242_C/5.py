def solve(N):
    mod = 998244353
    dp = [[0] * 10 for _ in range(N + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, N + 1):
        for j in range(10):
            for k in range(10):
                if abs(j - k) <= 1:
                    dp[i][j] += dp[i - 1][k]
                    dp[i][j] %= mod
    return sum(dp[N]) % mod

if __name__ == '__main__':
    solve()