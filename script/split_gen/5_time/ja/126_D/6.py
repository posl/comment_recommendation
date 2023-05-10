def dfs(u, c):
    color[u] = c
    for v, w in adj[u]:
        if color[v] == -1:
            dfs(v, c ^ w)
n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append((v, w % 2))
    adj[v].append((u, w % 2))
color = [-1] * n
dfs(0, 0)
for c in color:
    print(c)
