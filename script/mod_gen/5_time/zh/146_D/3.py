def dfs(v, p):
    global k
    c = 0
    for u in g[v]:
        if u == p:
            continue
        c += 1
        if c == c2:
            c += 1
        k = max(k, c)
        color[(v, u)] = c
        dfs(u, v)
n = int(input())
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
k = 0
color = {}
for v in range(n):
    k = max(k, len(g[v]))
    if k == len(g[v]):
        c1 = v
    if k == len(g[v]) - 1:
        c2 = v
dfs(c1, -1)
print(k)
for i in range(n - 1):
    print(color[(i, i + 1)])

if __name__ == '__main__':
    dfs()