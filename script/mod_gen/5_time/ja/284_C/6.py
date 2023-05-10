def dfs(v):
    seen[v] = True
    for i in range(n):
        if G[v][i] == 0:
            continue
        if seen[i]:
            continue
        dfs(i)
n, m = map(int, input().split())
G = [[0] * n for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = 1
    G[b][a] = 1
seen = [False] * n
ans = 0
for i in range(n):
    if seen[i]:
        continue
    dfs(i)
    ans += 1
print(ans)

if __name__ == '__main__':
    dfs()