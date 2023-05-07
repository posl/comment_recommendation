def dfs(v, p, d):
    dist[v] = d
    for u in G[v]:
        if u == p:
            continue
        dfs(u, v, d + 1)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
dist = [0] * N
dfs(0, -1, 0)
ans = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    ans[p] += x
for i in range(N):
    print(ans[i] + dist[i])

if __name__ == '__main__':
    dfs()