def main():
    #读入数据
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    #初始化
    dp = [[float('inf')] * W for _ in range(H)]
    #动态规划
    for i in range(H):
        for j in range(W):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + C)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + C)
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + C)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + C)
            dp[i][j] = min(dp[i][j], A[i][j])
    #输出结果
    print(dp[-1][-1])

if __name__ == '__main__':
    main()