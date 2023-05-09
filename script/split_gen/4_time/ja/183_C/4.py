def dfs(now, visited, cost):
    if now == 0:
        return cost == k
    visited[now] = True
    ret = 0
    for i in range(n):
        if not visited[i]:
            ret += dfs(i, visited, cost + t[now][i])
    visited[now] = False
    return ret
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
print(dfs(0, visited, 0))
