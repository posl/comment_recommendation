def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    graph = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u-1][v-1] = 1
        graph[v-1][u-1] = 1
    visited = [False] * N
    count = 0
    for i in range(N):
        if not visited[i]:
            count += 1
            dfs(i, graph, visited)
    print(count)
