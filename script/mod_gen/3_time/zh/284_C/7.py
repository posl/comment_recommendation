def dfs(v):
    seen[v] = True
    for i in range(n):
        if graph[v][i] == 0:
            continue
        if seen[i]:
            continue
        dfs(i)
n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = 1
    graph[v][u] = 1
ans = 0
seen = [False] * n
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    ans += 1
print(ans)

if __name__ == '__main__':
    dfs()