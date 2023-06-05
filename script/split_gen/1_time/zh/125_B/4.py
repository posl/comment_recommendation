def solve():
    # 读入数据
    N = int(input())
    V = [int(item) for item in input().split()]
    C = [int(item) for item in input().split()]
    # 初始化dp
    dp = [[0 for i in range(51)] for j in range(51)]
    # 状态转移
    for i in range(N):
        for j in range(51):
            if j < C[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - C[i]] + V[i])
    # 打印结果
    print(dp[N][50])
solve()
