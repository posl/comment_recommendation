def floyd_warshall(n, graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if __name__ == '__main__':
    floyd_warshall()