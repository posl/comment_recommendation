def dfs(v, p):
    global dep
    dep[v] = dep[p]+1
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v)
n, x, y = map(int, input().split())
x -= 1
y -= 1
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
dep = [0]*n
dfs(x, x)
print(dep[y]-1)

if __name__ == '__main__':
    dfs()