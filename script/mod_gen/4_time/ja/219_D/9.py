def solve():
    N = int(input())
    X,Y = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    INF = 10**18
    dp = [[[INF for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(1,N+1):
        a,b = AB[i-1]
        for j in range(X+1):
            for k in range(Y+1):
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])
                if j >= a and k >= b:
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-a][k-b] + 1)
    if dp[N][X][Y] == INF:
        print(-1)
    else:
        print(dp[N][X][Y])
solve()
