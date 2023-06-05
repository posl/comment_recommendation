def dfs(now, visited, cost, n, k):
    visited[now] = True
    if all(visited):
        if cost == k:
            return 1
        else:
            return 0
    ret = 0
    for next in range(n):
        if not visited[next]:
            ret += dfs(next, visited, cost + T[now][next], n, k)
    visited[now] = False
    return ret
n, k = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
print(dfs(0, visited, 0, n, k))
