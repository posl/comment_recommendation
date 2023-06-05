def dfs(v):
    global k
    if visited[v]:
        return
    visited[v] = True
    for i in range(1, n+1):
        if G[v][i] == 1:
            dfs(i)
        elif G[v][i] == 2:
            k += 1
            G[v][i] = 0
            G[i][v] = 0
            dfs(i)
n, m = map(int, input().split())
G = [[0] * (n+1) for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1
visited = [False] * (n+1)
k = 0
dfs(1)
print(k)

if __name__ == '__main__':
    dfs()