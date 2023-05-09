def dfs(v, p, d):
    global D
    D[v] = d
    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v, d+1)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)
D = [0] * N
dfs(0, -1, 0)
cnt = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p = p-1
    cnt[p] += x
for i in range(N):
    cnt[i] += D[i]
print(*cnt)

if __name__ == '__main__':
    dfs()