def dfs(v):
    visited[v] = True
    for j in range(len(G[v])):
        if visited[G[v][j][0]] == False:
            ans[G[v][j][0]] += ans[v] + G[v][j][1]
            dfs(G[v][j][0])
    return
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
visited = [False for _ in range(N)]
ans = [0 for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append((b - 1, 1))
    G[b - 1].append((a - 1, 1))
for _ in range(Q):
    p, x = map(int, input().split())
    ans[p - 1] += x
dfs(0)
for i in range(N):
    print(ans[i], end = ' ')
