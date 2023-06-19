def dfs(v):
    seen[v] = True
    for i in range(n):
        if not seen[i] and g[v][i] == 1:
            dfs(i)
n, m = map(int, input().split())
g = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1][b-1] = g[b-1][a-1] = 1
seen = [False for _ in range(n)]
ans = 0
for i in range(n):
    if not seen[i]:
        dfs(i)
        ans += 1
print(ans)

if __name__ == '__main__':
    dfs()