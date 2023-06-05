def dfs(v):
    seen[v] = True
    for i in range(n):
        if G[v][i] == 1 and seen[i] == False:
            dfs(i)
n, m = map(int, input().split())
G = [[0 for i in range(n)] for j in range(n)]
seen = [False for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    G[u-1][v-1] = 1
    G[v-1][u-1] = 1
ans = 0
for i in range(n):
    if seen[i] == False:
        dfs(i)
        ans += 1
print(ans)

if __name__ == '__main__':
    dfs()