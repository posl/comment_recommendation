def main():
    from collections import defaultdict
    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    visited = [False] * (n + 1)
    def dfs(v):
        visited[v] = True
        for i in g[v]:
            if not visited[i]:
                dfs(i)
    ans = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            ans += 1
    print(ans)
