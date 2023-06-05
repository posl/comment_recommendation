def main():
    # 读入数据
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    # dp[i][j] 表示从(i, j)出发到达右下角的最大步数
    dp = [[0] * W for _ in range(H)]
    dp[H - 1][W - 1] = 1
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if i == H - 1 and j == W - 1:
                continue
            if C[i][j] == '#':
                continue
            if i == H - 1:
                dp[i][j] = dp[i][j + 1]
            elif j == W - 1:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
    print(dp[0][0])
