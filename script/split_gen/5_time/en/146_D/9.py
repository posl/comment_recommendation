def dfs(v, p, c):
    global color
    color[c] += 1
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v, c)
    return
N = int(input())
g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
color = [0] * N
dfs(0, -1, 0)
print(max(color))
for i in range(N-1):
    print(color[i+1] if color[i+1] > 0 else 1)
