def dfs(v, p, c):
    global color
    color[c] += 1
    for u in G[v]:
        if u == p:
            continue
        dfs(u, v, c)
N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
color = [0] * N
dfs(0, -1, 0)
K = max(color)
print(K)
for i in range(N-1):
    print(color[i])
