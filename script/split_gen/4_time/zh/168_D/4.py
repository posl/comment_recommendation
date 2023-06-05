def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if visited[next_v]:
            continue
        dfs(next_v)
        if dp[next_v] == 0:
            dp[v] = next_v
            return
        elif dp[v] == 0:
            dp[v] = dp[next_v]
        else:
            dp[v] = -1
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
dp = [0] * (n + 1)
dfs(1)
