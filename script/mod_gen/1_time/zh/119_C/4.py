def getMinMP(n, a, b, c, ls):
    ls.sort(reverse=True)
    dp = [[[float('inf') for i in range(3001)] for j in range(3001)] for k in range(3001)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(3001):
            for k in range(3001):
                for l in range(3001):
                    if j >= ls[i]:
                        dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j-ls[i]][k]+l)
                    if k >= ls[i]:
                        dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k-ls[i]]+l)
                    dp[i+1][min(j+ls[i], 3000)][k] = min(dp[i+1][min(j+ls[i], 3000)][k], dp[i][j][k]+l)
                    dp[i+1][j][min(k+ls[i], 3000)] = min(dp[i+1][j][min(k+ls[i], 3000)], dp[i][j][k]+l)
                    dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
    res = float('inf')
    for i in range(3001):
        for j in range(3001):
            if i >= a and j >= b and i+j <= 3000:
                res = min(res, dp[n][i][j]+abs(i-a)+abs(j-b)+abs(i+j-c))
    return res

if __name__ == '__main__':
    getMinMP()