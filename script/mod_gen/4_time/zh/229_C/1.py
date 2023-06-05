def main():
    #读取数据
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #动态规划
    #dp[i][j]表示从前i种奶酪中选出总重量j的最大美味度
    #dp[i][j] = max(dp[i-1][j], dp[i-1][j-B[i]]+A[i], dp[i-1][j-2*B[i]]+2*A[i], ...)
    #dp[i][j-B[i]] = max(dp[i-1][j-B[i]], dp[i-1][j-2*B[i]]+A[i], ...)
    #dp[i][j] = max(dp[i-1][j], dp[i][j-B[i]]+A[i])
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j >= B[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-B[i-1]]+A[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N][W])

if __name__ == '__main__':
    main()