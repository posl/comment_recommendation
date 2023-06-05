def main():
    # 读入数据
    x, y = map(int, input().split())
    # 初始化
    dp = [[0] * (y + 1) for _ in range(x + 1)]
    dp[0][0] = 1
    # 动态规划
    for i in range(x + 1):
        for j in range(y + 1):
            if i + 1 <= x and j + 2 <= y:
                dp[i + 1][j + 2] = (dp[i + 1][j + 2] + dp[i][j]) % (10 ** 9 + 7)
            if i + 2 <= x and j + 1 <= y:
                dp[i + 2][j + 1] = (dp[i + 2][j + 1] + dp[i][j]) % (10 ** 9 + 7)
    # 输出结果
    print(dp[x][y])

if __name__ == '__main__':
    main()