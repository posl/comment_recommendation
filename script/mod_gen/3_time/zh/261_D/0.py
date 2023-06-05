def solve():
    # 读入数据
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    CY = [list(map(int, input().split())) for i in range(M)]
    # print(N, M)
    # print(X)
    # print(CY)
    # dp[i][j]表示第i次抛硬币，连续抛出j次正面时，可以得到的最大金额
    # dp[i][j] = max(dp[i-1][j-1]+X[i], dp[i-1][j])
    dp = [[0 for j in range(N+1)] for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = max(dp[i-1][j-1]+X[i-1], dp[i-1][j])
    # print(dp)
    # 计算最大金额
    ans = 0
    for i in range(1, M+1):
        C, Y = CY[i-1]
        for j in range(1, N+1):
            ans = max(ans, dp[j][C]+Y)
    print(ans)

if __name__ == '__main__':
    solve()