def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
seen = [False]*n
ans = 0
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    ans += 1
print(ans)

if __name__ == '__main__':
    dfs()