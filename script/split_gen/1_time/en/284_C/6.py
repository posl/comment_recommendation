def main():
    n, m = map(int, input().split())
    if m == 0:
        print(n)
        return
    edges = [list(map(int, input().split())) for _ in range(m)]
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i, graph, visited)
    print(count)
