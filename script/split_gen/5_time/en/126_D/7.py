def dfs(v, p, d):
    global color
    color[v] = d
    for i in range(len(e[v])):
        if e[v][i] == p:
            continue
        if w[v][i] % 2 == 0:
            dfs(e[v][i], v, d)
        else:
            dfs(e[v][i], v, 1 - d)
n = int(input())
e = [[] for _ in range(n)]
w = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, ww = map(int, input().split())
    e[u - 1].append(v - 1)
    e[v - 1].append(u - 1)
    w[u - 1].append(ww)
    w[v - 1].append(ww)
color = [-1] * n
dfs(0, -1, 0)
for i in range(n):
    print(color[i])
