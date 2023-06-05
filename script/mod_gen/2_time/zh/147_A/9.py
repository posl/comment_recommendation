def dfs(v, p):
    global k
    global color
    c = 1
    for u in g[v]:
        if u == p:
            continue
        if c == color[v]:
            c += 1
        color[u] = c
        k = max(k, c)
        dfs(u, v)
        c += 1
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
color = [-1] * n
color[0] = 1
k = 1
dfs(0, -1)
print(k)
for i in range(n - 1):
    print(color[i + 1])

if __name__ == '__main__':
    dfs()