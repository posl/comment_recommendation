def dfs(v, p):
    for i in to[v]:
        if i != p:
            cnt[i] += cnt[v]
            dfs(i, v)
n, q = map(int, input().split())
to = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)
cnt = [0] * n
for i in range(q):
    p, x = map(int, input().split())
    p -= 1
    cnt[p] += x
dfs(0, -1)
print(*cnt)
