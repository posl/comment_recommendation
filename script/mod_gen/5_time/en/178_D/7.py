def solve():
    s = int(input())
    dp = [[0 for i in range(s+1)] for j in range(s+1)]
    dp[0][0] = 1
    for i in range(3, s+1):
        for j in range(s+1):
            if j-i >= 0:
                dp[i][j] = (dp[i-1][j] + dp[i][j-i]) % (10**9+7)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[s][s])
solve()

if __name__ == '__main__':
    solve()