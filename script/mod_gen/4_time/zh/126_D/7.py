def dfs(u, c):
    color[u] = c
    for v, w in G[u]:
        if color[v] == -1:
            dfs(v, c ^ w)
N = int(input())
G = [[] for i in range(N)]
color = [-1] * N
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w % 2))
    G[v].append((u, w % 2))
dfs(0, 0)
for i in range(N):
    print(color[i])

if __name__ == '__main__':
    dfs()