def solve():
    # 读取输入
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    # 生成组合
    C = [[0] * N for _ in range(1 << N)]
    for i in range(1 << N):
        for j in range(N):
            if (i >> j) & 1:
                for k in range(j + 1, N):
                    if (i >> k) & 1:
                        C[i][j] += A[j][k]
    # 动态规划
    dp = [0] * (1 << N)
    for i in range(1, 1 << N):
        for j in range(N):
            if (i >> j) & 1:
                dp[i] = max(dp[i], dp[i - (1 << j)] + C[i][j])
    # 输出结果
    print(dp[-1])
