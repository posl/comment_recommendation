def dfs(v, c):
    color[v] = c
    for to in g[v]:
        if color[to] == c:
            return False
        if color[to] == 0 and not dfs(to, -c):
            return False
    return True
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
color = [0] * n
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            ans += 1
print(ans * (n - ans) - m)

if __name__ == '__main__':
    dfs()