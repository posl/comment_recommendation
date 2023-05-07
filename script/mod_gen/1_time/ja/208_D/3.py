def main():
    N, M = map(int, input().split())
    G = [[float('inf')]*N for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        G[A-1][B-1] = C
    for i in range(N):
        G[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k]+G[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if G[i][j] > G[i][k]+G[k][j]:
                    ans += G[i][k]+G[k][j]
    print(ans)

if __name__ == '__main__':
    main()