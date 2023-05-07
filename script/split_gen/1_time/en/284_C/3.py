def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    graph = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    visited = [False] * N
    count = 0
    for i in range(N):
        if not visited[i]:
            dfs(graph, visited, i)
            count += 1
    print(count)
