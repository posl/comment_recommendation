def solve():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input()
    #print(N,K,R,S,P,T)
    #dp[i][0]表示第i轮出石头时的最大分数
    #dp[i][1]表示第i轮出剪刀时的最大分数
    #dp[i][2]表示第i轮出布时的最大分数
    dp = [[0 for i in range(3)] for j in range(N)]
    for i in range(N):
        if T[i] == 'r':
            dp[i][0] = max(dp[i][0],dp[i-1][1]+S,dp[i-1][2]+P)
            dp[i][1] = max(dp[i][1],dp[i-1][0])
            dp[i][2] = max(dp[i][2],dp[i-1][0])
        elif T[i] == 's':
            dp[i][0] = max(dp[i][0],dp[i-1][1])
            dp[i][1] = max(dp[i][1],dp[i-1][2]+P,dp[i-1][0]+R)
            dp[i][2] = max(dp[i][2],dp[i-1][1])
        else:
            dp[i][0] = max(dp[i][0],dp[i-1][2]+P,dp[i-1][1]+S)
            dp[i][1] = max(dp[i][1],dp[i-1][0])
            dp[i][2] = max(dp[i][2],dp[i-1][0])
        if i >= K:
            dp[i][0] = max(dp[i][0],dp[i-K][0],dp[i-K][1],dp[i-K][2])
            dp[i][1] = max(dp[i][1],dp[i-K][0],dp[i-K][1],dp[i-K][2])
            dp[i][2] = max(dp[i][2],dp[i-K][0],dp[i-K][1],dp[i-K][2])
    #print(dp)
    print(max(dp[N-1][0],dp[N-1][1],dp[N-1][2]))
solve()
