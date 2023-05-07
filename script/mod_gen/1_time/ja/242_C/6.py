def solve(n):
    dp = [[0] * 10 for _ in range(n+1)]
    for i in range(1,10):
        dp[1][i] = 1
    for i in range(1,n):
        for j in range(10):
            if j == 0:
                dp[i+1][j] = dp[i][j+1]
            elif j == 9:
                dp[i+1][j] = dp[i][j-1]
            else:
                dp[i+1][j] = (dp[i][j-1] + dp[i][j+1]) % 998244353
    return sum(dp[n]) % 998244353

if __name__ == '__main__':
    solve()