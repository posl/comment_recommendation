def dfs(G, v, c):
    color[v] = c
    for t in G[v]:
        if color[t] == c:
            return False
        if color[t] == 0 and not dfs(G, t, -c):
            return False
    return True
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
color = [0] * N

if __name__ == '__main__':
    dfs()