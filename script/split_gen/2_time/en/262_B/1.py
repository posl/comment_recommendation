def main():
    n, m = map(int, input().split())
    graph = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = 1
        graph[v][u] = 1
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if graph[i][j] == 1 and graph[j][k] == 1 and graph[k][i] == 1:
                    count += 1
    print(count)
