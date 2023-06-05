def solve(n):
    dp = [[0 for _ in range(10)] for _ in range(n+1)]
    for i in range(1,10):
        dp[1][i] = 1
    for i in range(2,n+1):
        for j in range(10):
            for k in range(10):
                if abs(j-k)<=1:
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %= 998244353
    return sum(dp[n])%998244353

if __name__ == '__main__':
    solve()