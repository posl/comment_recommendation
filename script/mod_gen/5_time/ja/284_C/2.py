def dfs(v):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(next_v)
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
seen = [False] * N
ans = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(v)
    ans += 1
print(ans)

if __name__ == '__main__':
    dfs()