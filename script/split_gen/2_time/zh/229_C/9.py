def solve():
    N,W = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1,N+1):
        for w in range(1,W+1):
            if w >= B[i-1]:
                dp[i][w] = max(dp[i-1][w-B[i-1]]+A[i-1],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    print(dp[N][W])
