def dfs(now, par):
    for nex in G[now]:
        if nex == par: continue
        dist[nex] = dist[now] + 1
        dfs(nex, now)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
dist = [0] * N
dfs(0, -1)
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")

if __name__ == '__main__':
    dfs()