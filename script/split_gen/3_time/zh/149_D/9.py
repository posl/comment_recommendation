def solve():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input()
    #dp[i][j]表示在第i轮时，我方手势为j时的最大分数
    dp = [[0,0,0] for i in range(N+1)]
    for i in range(N):
        #我方手势为石头
        if T[i] == 'r':
            dp[i+1][0] = max(dp[i+1][0],dp[i][1]+P,dp[i][2]+P)
            dp[i+1][1] = max(dp[i+1][1],dp[i][0])
            dp[i+1][2] = max(dp[i+1][2],dp[i][0])
        #我方手势为剪刀
        if T[i] == 's':
            dp[i+1][0] = max(dp[i+1][0],dp[i][1])
            dp[i+1][1] = max(dp[i+1][1],dp[i][0]+R,dp[i][2]+R)
            dp[i+1][2] = max(dp[i+1][2],dp[i][0])
        #我方手势为布
        if T[i] == 'p':
            dp[i+1][0] = max(dp[i+1][0],dp[i][1])
            dp[i+1][1] = max(dp[i+1][1],dp[i][0])
            dp[i+1][2] = max(dp[i+1][2],dp[i][0]+S,dp[i][1]+S)
        for j in range(3):
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
        if i+1>=K:
            for j in range(3):
                for k in range(3):
                    if j!=k:
                        dp[i+1][j] = max(dp[i+1][j],dp[i-K+1][k]+dp[i+1][j])
    print(max(dp[N]))
