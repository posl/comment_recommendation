def dfs(v):
    visited[v] = True
    for i in range(n):
        if not visited[i] and g[v][i]:
            dfs(i)
n, m = map(int, input().split())
g = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1][b-1] = g[b-1][a-1] = True
visited = [False] * n
ans = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)

if __name__ == '__main__':
    dfs()