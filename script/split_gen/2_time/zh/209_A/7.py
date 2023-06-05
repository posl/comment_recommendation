def main():
    n,m = map(int, input().split())
    graph = [[float('inf') for i in range(n)] for j in range(n)]
    for i in range(m):
        a,b,c = map(int, input().split())
        graph[a-1][b-1] = c
    for i in range(n):
        graph[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    res = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[i][j] == graph[i][k] + graph[k][j]:
                    res += graph[i][j]
    print(res)
