def dfs(v):
    seen[v] = True
    group[v] = cnt
    for i in range(n):
        if not seen[i] and g[v][i] == 1:
            dfs(i)
n, m = map(int, input().split())
g = [[0] * n for i in range(n)]
seen = [False] * n
group = [None] * n
cnt = 0
for i in range(m):
    u, v = map(int, input().split())
    g[u - 1][v - 1] = 1
    g[v - 1][u - 1] = 1
for i in range(n):
    if not seen[i]:
        cnt += 1
        dfs(i)
print(cnt)

if __name__ == '__main__':
    dfs()