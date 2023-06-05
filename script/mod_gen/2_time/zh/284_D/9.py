def dfs(i):
    visited[i] = 1
    for j in range(n):
        if visited[j] == 0 and G[i][j] == 1:
            dfs(j)
n, m = map(int, input().split())
G = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    G[a-1][b-1] = 1
    G[b-1][a-1] = 1
visited = [0 for i in range(n)]
ans = 0
for i in range(n):
    if visited[i] == 0:
        dfs(i)
        ans += 1
print(ans)

if __name__ == '__main__':
    dfs()