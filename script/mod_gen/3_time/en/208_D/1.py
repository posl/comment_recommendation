def solve():
    N, M = map(int, input().split())
    G = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        G[i][i] = 0
    for _ in range(M):
        A, B, C = map(int, input().split())
        G[A - 1][B - 1] = C
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ans += G[i][k] if G[i][k] < float('inf') and G[i][k] == G[i][j] else 0
    print(ans)
solve()

if __name__ == '__main__':
    solve()