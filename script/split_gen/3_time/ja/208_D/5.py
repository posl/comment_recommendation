def main():
    N, M = map(int, input().split())
    graph = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        graph[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a-1][b-1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if graph[i][k] + graph[k][j] == graph[i][j]:
                    ans += graph[i][j]
    print(ans)
