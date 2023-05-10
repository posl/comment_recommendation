def main():
    N, M = map(int, input().split())
    G = [[float('inf')]*N for _ in range(N)]
    for i in range(N):
        G[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[a-1][b-1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k]+G[k][j])
    ans = 0
    for s in range(N):
        for t in range(N):
            for k in range(N):
                if s == t or s == k or t == k:
                    continue
                if G[s][t] == G[s][k]+G[k][t]:
                    ans += G[s][t]
    print(ans)

if __name__ == '__main__':
    main()