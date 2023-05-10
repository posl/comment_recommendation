def dfs(v, visited, n, k, t):
    visited[v] = 1
    if sum(visited) == n:
        if k == 0:
            return 1
        else:
            return 0
    ret = 0
    for i in range(n):
        if visited[i] == 0:
            ret += dfs(i, visited, n, k-t[v][i], t)
    visited[v] = 0
    return ret
n, k = map(int, input().split())
t = []
for _ in range(n):
    t.append(list(map(int, input().split())))
visited = [0]*n
print(dfs(0, visited, n, k, t))
