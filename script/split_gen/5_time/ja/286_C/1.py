def resolve():
    N,A,B = map(int,input().split())
    S = input()
    #print(N,A,B,S)
    #dp[i][j]は、i文字目まで見たときに、j文字を変える場合の最小値
    dp = [[float('inf')]*(N+1) for i in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N+1):
            if S[i] == S[N-1-i]:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j])
            else:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j]+A)
                if j < N:
                    dp[i+1][j+1] = min(dp[i+1][j+1],dp[i][j]+B)
    ans = float('inf')
    for i in range(N+1):
        ans = min(ans,dp[N][i]+A*i)
    print(ans)
