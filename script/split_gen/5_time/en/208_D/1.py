def solve():
    N,M = map(int,input().split())
    A,B,C = [],[],[]
    for _ in range(M):
        a,b,c = map(int,input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    for i in range(M):
        A[i] -= 1
        B[i] -= 1
    dp = [[[float('inf') for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i][0] = 0
    for i in range(M):
        dp[A[i]][B[i]][0] = C[i]
    for k in range(1,N):
        for s in range(N):
            for t in range(N):
                for u in range(N):
                    if dp[s][u][k-1] != float('inf') and dp[u][t][0] != float('inf'):
                        dp[s][t][k] = min(dp[s][t][k], dp[s][u][k-1] + dp[u][t][0])
    ans = 0
    for s in range(N):
        for t in range(N):
            for k in range(N):
                if dp[s][t][k] != float('inf'):
                    ans += dp[s][t][k]
    print(ans)
