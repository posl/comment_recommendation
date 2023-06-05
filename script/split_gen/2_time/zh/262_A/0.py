def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    #dp[i][j] 表示第i次投掷后，连续投掷j次且获得奖励的最大金额
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    #初始化
    for i in range(1, N+1):
        dp[i][0] = dp[i-1][0] + X[i-1]
    #状态转移
    for i in range(1, N+1):
        for j in range(1, i+1):
            dp[i][j] = max(dp[i-1][j-1] + X[i-1], dp[i-1][j])
            if j in C:
                dp[i][0] = max(dp[i][0], dp[i][j] + Y[C.index(j)])
    print(max(dp[N]))
