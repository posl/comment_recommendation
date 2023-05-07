def main():
    M = int(input())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    P = list(map(int,input().split()))
    for i in range(8):
        P[i] -= 1
    INF = 10**10
    dp = [[INF]*9 for _ in range(1<<8)]
    for i in range(8):
        dp[1<<i][P[i]] = 0
    for S in range(1<<8):
        for v in range(9):
            for nv in G[v]:
                for i in range(8):
                    if (S>>i)&1:
                        continue
                    if P[i] == nv:
                        dp[S|(1<<i)][nv] = min(dp[S|(1<<i)][nv],dp[S][v]+1)
    ans = min(dp[(1<<8)-1])
    if ans == INF:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()