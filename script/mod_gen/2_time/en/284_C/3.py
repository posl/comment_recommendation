def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (N + 1)
    count = 0
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1
    print(count)

if __name__ == '__main__':
    main()