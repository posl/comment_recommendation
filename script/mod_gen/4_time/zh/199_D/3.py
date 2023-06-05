def dfs(u, c):
    color[u] = c
    for i in range(N):
        if G[u][i] == 0:
            continue
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True
N, M = map(int, input().split())
G = [[0] * N for _ in range(N)]
color = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1][b - 1] = G[b - 1][a - 1] = 1

if __name__ == '__main__':
    dfs()