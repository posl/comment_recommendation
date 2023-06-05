def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)
N, M = map(int, input().split())
graph = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
seen = [False] * N
count = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(v)
    count += 1
print(count)

if __name__ == '__main__':
    dfs()