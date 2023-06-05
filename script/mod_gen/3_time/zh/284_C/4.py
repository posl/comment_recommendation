def dfs(v):
    visited[v] = True
    for i in range(n):
        if G[v][i] and not visited[i]:
            dfs(i)
n, m = map(int, input().split())
G = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    G[u-1][v-1] = G[v-1][u-1] = True
visited = [False] * n
cnt = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)

if __name__ == '__main__':
    dfs()