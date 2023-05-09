def dfs(v, p):
    for u in G[v]:
        if u == p: continue
        cnt[u] += cnt[v]
        dfs(u, v)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)
cnt = [0]*N
for _ in range(Q):
    p, x = map(int, input().split())
    cnt[p-1] += x
dfs(0, -1)
print(*cnt)

if __name__ == '__main__':
    dfs()