def dfs(now, color):
    global res
    visited[now] = color
    if color == 1:
        res += 1
    for nxt in G[now]:
        if visited[nxt] == -1:
            dfs(nxt, 1 - color)
        elif visited[nxt] == color:
            print(0)
            exit()
    return
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
visited = [-1] * N
res = 0
dfs(0, 0)
print(res * (N - res) - M)
