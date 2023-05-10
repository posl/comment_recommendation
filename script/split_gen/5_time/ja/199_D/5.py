def dfs(v, c):
    color[v] = c
    for i in range(len(graph[v])):
        if color[graph[v][i]] == c:
            return False
        if color[graph[v][i]] == 0 and not dfs(graph[v][i], -c):
            return False
    return True
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
color = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            r = color.count(1)
            b = color.count(-1)
            ans += r * (r - 1) // 2 + b * (b - 1) // 2
        else:
            ans = 0
            break
print(ans)
