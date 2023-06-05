def solve():
    N,W = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #dp[i][j]表示：前i种奶酪中，总重量为j时的最大美味值
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,W+1):
            if j >= B[i-1]:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-B[i-1]]+A[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    #print(dp)
    print(dp[N][W])
solve()
