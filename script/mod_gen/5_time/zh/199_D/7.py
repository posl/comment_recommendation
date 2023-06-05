def dfs(v, c):
    global ans
    color[v] = c
    if v == N - 1:
        ans += 1
        return
    for i in range(N):
        if G[v][i] == 1 and color[i] == -1:
            dfs(i, 0)
            dfs(i, 1)
            dfs(i, 2)
            break
N, M = map(int, input().split())
G = [[0] * N for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1][b - 1] = 1
    G[b - 1][a - 1] = 1
color = [-1] * N
ans = 0
dfs(0, 0)
dfs(0, 1)
dfs(0, 2)
print(ans)

if __name__ == '__main__':
    dfs()