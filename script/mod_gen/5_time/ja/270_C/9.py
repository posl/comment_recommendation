def dfs(v, p):
    for u in G[v]:
        if u == p:
            continue
        dist[u] = dist[v] + 1
        dfs(u, v)
N, X, Y = map(int, input().split())
X -= 1
Y -= 1
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
dist = [0] * N
dfs(X, -1)
print(*sorted(dist[Y:]))

if __name__ == '__main__':
    dfs()