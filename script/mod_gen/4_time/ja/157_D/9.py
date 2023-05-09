def dfs(v, c):
    color[v] = c
    for i in range(len(g[v])):
        if color[g[v][i]] == c:
            return False
        if color[g[v][i]] == 0 and not dfs(g[v][i], -c):
            return False
    return True
n, m, k = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
color = [0 for i in range(n)]
for i in range(n):
    if color[i] == 0:
        if not dfs(i, 1):
            print(-1)
            exit()
ans = [0 for i in range(n)]
for i in range(n):
    ans[i] = len(g[i])
for i in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if color[c] == color[d]:
        ans[c] -= 1
        ans[d] -= 1
print(*ans)

if __name__ == '__main__':
    dfs()