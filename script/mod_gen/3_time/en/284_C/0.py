def dfs(G, v, seen):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v, seen)
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)
seen = [False] * N
count = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(G, v, seen)
    count += 1
print(count)

if __name__ == '__main__':
    dfs()