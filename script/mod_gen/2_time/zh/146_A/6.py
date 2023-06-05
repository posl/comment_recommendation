def solve(x, y):
    # 1. 构造二维数组
    # 2. 初始化数组
    # 3. 递推
    # 4. 返回结果
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = 1
    for i in range(x+1):
        for j in range(y+1):
            if i+1 <= x and j+2 <= y:
                dp[i+1][j+2] = (dp[i+1][j+2] + dp[i][j]) % (10**9+7)
            if i+2 <= x and j+1 <= y:
                dp[i+2][j+1] = (dp[i+2][j+1] + dp[i][j]) % (10**9+7)
    return dp[x][y]

if __name__ == '__main__':
    solve()