def countTriangles(graph, N):
    count = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if graph[i][j] == 1:
                for k in range(j+1, N+1):
                    if graph[j][k] == 1 and graph[k][i] == 1:
                        count += 1
    return count
N, M = map(int, input().split())
graph = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
print(countTriangles(graph, N))
