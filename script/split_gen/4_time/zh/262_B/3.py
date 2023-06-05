def main():
    N, M = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1][v-1] = 1
        graph[v-1][u-1] = 1
    ans = 0
    for a in range(N):
        for b in range(a+1, N):
            if graph[a][b] != 1:
                continue
            for c in range(b+1, N):
                if graph[b][c] == 1 and graph[c][a] == 1:
                    ans += 1
    print(ans)
