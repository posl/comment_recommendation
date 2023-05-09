def main():
    M = int(input())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    p = list(map(int, input().split()))
    for i in range(8):
        p[i] -= 1
    p[8] = 8
    INF = 10**9
    dp = [[INF]*9 for _ in range(1<<8)]
    dp[0][p[8]] = 0
    for S in range(1<<8):
        for i in range(9):
            if dp[S][i] == INF:
                continue
            for j in G[i]:
                if (S>>j)&1:
                    continue
                dp[S|(1<<j)][j] = min(dp[S|(1<<j)][j], dp[S][i]+(p[j]!=j))
    print(dp[-1][8] if dp[-1][8] < INF else -1)

if __name__ == '__main__':
    main()