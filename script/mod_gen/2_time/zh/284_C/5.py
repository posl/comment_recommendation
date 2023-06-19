def dfs(v):
    visited[v] = True
    for i in range(n):
        if not visited[i] and G[v][i]:
            dfs(i)
n, m = map(int, input().split())
G = [[False for i in range(n)] for j in range(n)]
for i in range(m):
    s, t = map(int, input().split())
    G[s-1][t-1] = G[t-1][s-1] = True
visited = [False for i in range(n)]
ans = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)

if __name__ == '__main__':
    dfs()