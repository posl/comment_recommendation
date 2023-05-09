def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    def dfs(v):
        visited[v] = True
        for u in edges[v]:
            if visited[u]:
                continue
            dfs(u)
    visited = [False] * n
    dfs(0)
    print("Yes" if all(visited) else "No")
