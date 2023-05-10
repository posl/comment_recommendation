def dfs(v, c):
    color[v] = c
    for i in g[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
color = [0]*n
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            ans += 1
print(ans)

if __name__ == '__main__':
    dfs()