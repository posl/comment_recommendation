def dfs(v, p):
    for u, w in G[v]:
        if u == p:
            continue
        dist[u] = dist[v] + w
        dfs(u, v)
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))
dist = [0] * N
dfs(0, -1)
ans = 0
for i in range(N):
    ans += dist[i]
for i in range(N):
    dist[i] = -dist[i]
dist.sort()
ans += dist[0] + dist[1]
print(ans)

if __name__ == '__main__':
    dfs()