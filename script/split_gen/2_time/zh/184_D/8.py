def solve():
    # 读入数据
    a, b, c = map(int, input().split())
    # 用动态规划求解
    # dp[i][j][k]: 从(i, j, k)状态开始，直到100个相同颜色的硬币出现的期望操作次数
    dp = [[[0] * 100 for _ in range(100)] for _ in range(100)]
    for i in range(99, -1, -1):
        for j in range(99, -1, -1):
            for k in range(99, -1, -1):
                if i == 99 and j == 99 and k == 99:
                    continue
                if i + j + k == 0:
                    continue
                # 求解dp[i][j][k]
                dp[i][j][k] = (i * dp[i + 1][j][k] + j * dp[i][j + 1][k] + k * dp[i][j][k + 1]) / (i + j + k) + 1
    # 输出结果
    print(dp[a][b][c])
