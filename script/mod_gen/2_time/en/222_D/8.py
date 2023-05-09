def solve(arr1, arr2):
    mod = 998244353
    dp = [[0 for i in range(3001)] for j in range(3001)]
    dp[0][0] = 1
    for i in range(len(arr1)):
        for j in range(arr1[i], arr2[i] + 1):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod
            dp[i + 1][j] += dp[i + 1][j - 1]
            dp[i + 1][j] %= mod
    return dp[len(arr1)][arr2[len(arr1) - 1]]

if __name__ == '__main__':
    solve()