def main():
    N, M = map(int, input().split())
    edge = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        edge[u - 1][v - 1] = 1
        edge[v - 1][u - 1] = 1
    ans = 0
    for a in range(N):
        for b in range(a + 1, N):
            for c in range(b + 1, N):
                if edge[a][b] == 1 and edge[b][c] == 1 and edge[c][a] == 1:
                    ans += 1
    print(ans)
