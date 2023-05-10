def main():
    N, X, Y = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N-1):
        graph[i][i+1] = 1
        graph[i+1][i] = 1
    graph[X-1][Y-1] = 1
    graph[Y-1][X-1] = 1
    for k in range(N-1):
        for i in range(N-1):
            for j in range(i+1, N):
                if graph[i][j] == 0 and graph[i][k] != 0 and graph[k][j] != 0:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    graph[j][i] = graph[i][j]
    for i in range(N-1):
        count = 0
        for j in range(i+1, N):
            if graph[i][j] != 0:
                count += 1
        print(count)
    return
