def dfs(v, p):
    global cnt
    cnt[v] += cnt[p]
    for i in g[v]:
        if i != p:
            dfs(i, v)
n, q = map(int, input().split())
g = [[] for _ in range(n)]
cnt = [0] * n
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    cnt[p] += x
dfs(0, 0)
print(*cnt)

if __name__ == '__main__':
    dfs()