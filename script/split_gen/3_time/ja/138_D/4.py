def dfs(now, prev):
    for next in edge[now]:
        if next == prev:
            continue
        counter[next] += counter[now]
        dfs(next, now)
N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
counter = [0] * N
for i in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
for i in range(Q):
    p, x = map(int, input().split())
    counter[p-1] += x
dfs(0, -1)
print(*counter)
