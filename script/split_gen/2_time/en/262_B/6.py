def main():
    N, M = map(int, input().split())
    graph = [[False for j in range(N)] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u - 1][v - 1] = True
        graph[v - 1][u - 1] = True
    count = 0
    for a in range(N - 2):
        for b in range(a + 1, N - 1):
            for c in range(b + 1, N):
                if graph[a][b] and graph[b][c] and graph[c][a]:
                    count += 1
    print(count)
