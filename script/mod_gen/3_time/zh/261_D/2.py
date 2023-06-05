def main():
    # 读入数据
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    # print(N, M)
    # print(X)
    # print(C)
    # print(Y)
    # 初始化
    dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 0
    # 动态规划
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            # 投掷硬币为正面，计数器加1
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+X[i])
            # 投掷硬币为反面，计数器清零
            dp[i+1][0] = max(dp[i+1][0], dp[i][j])
    # print(dp)
    # 计算连胜奖金
    for i in range(N+1):
        for j in range(N+1):
            if dp[i][j] == -1:
                continue
            for k in range(M):
                if i+C[k] <= N:
                    dp[i+C[k]][j] = max(dp[i+C[k]][j], dp[i][j]+Y[k])
    # print(dp)
    # 计算最大金额
    ans = 0
    for i in range(N+1):
        for j in range(N+1):
            ans = max(ans, dp[i][j])
    print(ans)

if __name__ == '__main__':
    main()