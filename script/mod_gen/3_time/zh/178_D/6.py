def solve(S):
    dp = [[0 for i in range(S+1)] for j in range(S+1)]
    dp[0][0] = 1
    for i in range(3,S+1):
        for j in range(S+1):
            for k in range(j-i+1):
                dp[i][j] += dp[i-1][j-k]
                dp[i][j] %= 1000000007
    return dp[S][S]

if __name__ == '__main__':
    solve()