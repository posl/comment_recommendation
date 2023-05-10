def dfs(v, p, g, d):
    for nv in g[v]:
        if nv == p:
            continue
        d[nv] = d[v] + 1
        dfs(nv, v, g, d)
n, x, y = map(int, input().split())
x -= 1
y -= 1
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
d = [0]*n
dfs(x, -1, g, d)
print(d[y])

if __name__ == '__main__':
    dfs()