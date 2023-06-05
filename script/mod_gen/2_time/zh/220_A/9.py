def lunchbox():
    # 读取数据
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 处理数据
    # dp[i][j][k] 表示前i个便当中，章鱼烧个数为j，鱼形蛋糕个数为k时，最少的便当数
    dp = [[[float('inf')] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(1, N + 1):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                dp[i][min(j + A[i - 1], X)][min(k + B[i - 1], Y)] = min(dp[i][min(j + A[i - 1], X)][min(k + B[i - 1], Y)], dp[i - 1][j][k] + 1)
    # 输出结果
    if dp[N][X][Y] == float('inf'):
        print(-1)
    else:
        print(dp[N][X][Y])

if __name__ == '__main__':
    lunchbox()