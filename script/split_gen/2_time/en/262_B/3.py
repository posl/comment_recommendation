def main():
    N, M = map(int, input().split())
    graph = [[False for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1][v - 1] = True
        graph[v - 1][u - 1] = True
    ans = 0
    for a in range(N):
        for b in range(a + 1, N):
            for c in range(b + 1, N):
                if graph[a][b] and graph[b][c] and graph[c][a]:
                    ans += 1
    print(ans)
