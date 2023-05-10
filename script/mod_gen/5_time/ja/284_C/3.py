def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
seen = [False] * N
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
count = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(v)
    count += 1
print(count)

if __name__ == '__main__':
    dfs()