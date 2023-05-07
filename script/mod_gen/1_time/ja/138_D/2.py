def dfs(v, p=-1):
    for nv in g[v]:
        if nv == p:
            continue
        cnt[nv] += cnt[v]
        dfs(nv, v)
n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
cnt = [0]*n
for _ in range(q):
    p, x = map(int, input().split())
    cnt[p-1] += x
dfs(0)
print(*cnt)

if __name__ == '__main__':
    dfs()