def dfs(v, c):
    if v == N:
        return 1
    if dp[v][c] != -1:
        return dp[v][c]
    ans = 0
    for i in range(3):
        if i == c:
            continue
        flag = True
        for j in range(N):
            if G[v][j] == 1 and i == color[j]:
                flag = False
                break
        if flag:
            color[v] = i
            ans += dfs(v + 1, i)
    dp[v][c] = ans
    return ans
N, M = map(int, input().split())
G = [[0] * N for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = 1
    G[b][a] = 1
dp = [[-1] * 3 for i in range(N)]
color = [-1] * N
print(dfs(0, -1))

if __name__ == '__main__':
    dfs()