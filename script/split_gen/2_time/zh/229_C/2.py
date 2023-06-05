def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #dp[i][j] 表示前i个物品，重量为j的时候，最大的美味度
    dp = [[0 for j in range(W+1)] for i in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j >= B[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-B[i]]+A[i]*B[i])
            else:
                dp[i+1][j] = dp[i][j]
    #print(dp)
    print(dp[N][W])
