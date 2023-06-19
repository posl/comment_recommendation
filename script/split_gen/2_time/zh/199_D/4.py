def dfs(v, c):
    global ans
    color[v] = c
    if v == n - 1:
        ans += 1
        return
    for i in range(n):
        if edge[v][i] == 1 and color[i] == -1:
            for j in range(3):
                if j != c:
                    dfs(i, j)
            break
n, m = map(int, input().split())
edge = [[0 for i in range(n)] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    edge[a - 1][b - 1] = 1
    edge[b - 1][a - 1] = 1
color = [-1 for i in range(n)]
ans = 0
dfs(0, 0)
print(ans * 3)
