def solve():
    N,W = [int(x) for x in input().split()]
    A = []
    B = []
    for i in range(N):
        a,b = [int(x) for x in input().split()]
        A.append(a)
        B.append(b)
    maxA = max(A)
    maxB = max(B)
    if maxA > 1000:
        return 0
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j < B[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j],dp[i+1][j-B[i]]+A[i])
    return dp[N][W]
