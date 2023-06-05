def dfs(v, c):
    color[v] = c
    for i in range(len(edges[v])):
        if color[edges[v][i]] == c:
            return False
        if color[edges[v][i]] == 0 and (not dfs(edges[v][i], -c)):
            return False
    return True
n, m = map(int, input().split())
edges = [[] for i in range(n)]
color = [0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            ans += 1
        else:
            print(0)
            exit()
print(3 ** ans)
