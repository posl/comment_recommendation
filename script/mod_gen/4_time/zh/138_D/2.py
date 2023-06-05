def dfs(v, p, d):
    global dst
    dst[v] += d
    for i in range(len(g[v])):
        if g[v][i] == p:
            continue
        dfs(g[v][i], v, d)
n, q = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
dst = [0] * n
for i in range(q):
    p, x = map(int, input().split())
    p -= 1
    dfs(p, -1, x)
print(*dst)

if __name__ == '__main__':
    dfs()