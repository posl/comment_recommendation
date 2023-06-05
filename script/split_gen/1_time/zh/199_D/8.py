def dfs(v, c):
    color[v] = c
    for i in range(len(g[v])):
        if color[g[v][i]] == c:
            return False
        if color[g[v][i]] == 0 and (not dfs(g[v][i], -c)):
            return False
    return True
n, m = map(int, input().split())
g = [[] for i in range(n)]
color = [0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            t = 0
            for j in range(n):
                if color[j] == 1:
                    t += 1
            ans += 3 ** t
print(ans)
