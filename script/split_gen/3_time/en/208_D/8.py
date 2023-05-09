def floyd_warshall(n, graph):
    # graph = [[-1 for j in range(n)] for i in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == -1 or graph[k][j] == -1:
                    continue
                if graph[i][j] == -1 or graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
