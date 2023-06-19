def dfs(v):
    visited[v] = True
    for i in range(1, n+1):
        if not visited[i] and g[v][i]:
            dfs(i)
n, m = map(int, input().split())
g = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u][v] = g[v][u] = True
visited = [False]*(n+1)
ans = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)

if __name__ == '__main__':
    dfs()