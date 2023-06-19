def solve():
    # 读入数据
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    # 从终点开始进行动态规划
    dp = [[0] * W for _ in range(H)]
    dp[H - 1][W - 1] = 1
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if C[i][j] == '#':
                continue
            if i + 1 < H:
                dp[i][j] += dp[i + 1][j]
            if j + 1 < W:
                dp[i][j] += dp[i][j + 1]
            dp[i][j] %= 1000000007
    print(dp[0][0])
solve()
