def solve(n, x, y, a, b):
    #dp[i][j][k]表示前i种便当中选出j个章鱼烧和k个鱼形蛋糕的最小便当数
    dp = [[[float('inf') for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                dp[i+1][min(x, j+a[i])][min(y, k+b[i])] = min(dp[i+1][min(x, j+a[i])][min(y, k+b[i])], dp[i][j][k] + 1)
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
    return dp[n][x][y] if dp[n][x][y] != float('inf') else -1

if __name__ == '__main__':
    solve()