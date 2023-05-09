def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    visited = [False] * (n + 1)
    def dfs(v):
        visited[v] = True
        for next_v in graph[v]:
            if not visited[next_v]:
                dfs(next_v)
    count = 0
    for v in range(1, n + 1):
        if not visited[v]:
            dfs(v)
            count += 1
    print(count)
