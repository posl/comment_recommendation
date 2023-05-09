def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    def dfs(v):
        if v in visited:
            return
        visited.add(v)
        for vv in graph[v]:
            dfs(vv)
    visited = set()
    ans = 0
    for i in range(N):
        if i not in visited:
            dfs(i)
            ans += 1
    print(ans)
