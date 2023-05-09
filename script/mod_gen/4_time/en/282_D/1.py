def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [0 for _ in range(N+1)]
    black = [0 for _ in range(N+1)]
    white = [0 for _ in range(N+1)]
    def dfs(v, color):
        visited[v] = 1
        if color == 0:
            black[v] = 1
        else:
            white[v] = 1
        for i in range(len(graph[v])):
            if visited[graph[v][i]] == 0:
                dfs(graph[v][i], 1-color)
    dfs(1, 0)
    black_count = sum(black)
    white_count = sum(white)
    print(black_count*white_count - M)

if __name__ == '__main__':
    main()