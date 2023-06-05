def dfs(v):
    visited[v] = True
    for i in range(n):
        if not visited[i] and g[v][i] == 1:
            dfs(i)
n, m = map(int, input().split())
g = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    g[u - 1][v - 1] = g[v - 1][u - 1] = 1
visited = [False for i in range(n)]
ans = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)

if __name__ == '__main__':
    dfs()