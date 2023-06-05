def dfs(u, c, d):
    color[u] = c
    depth[u] = d
    for v in G[u]:
        if depth[v] == -1:
            dfs(v, c^1, d+1)
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
color = [-1] * n
depth = [-1] * n
dfs(0, 0, 0)
for i in range(n):
    print(color[i])

if __name__ == '__main__':
    dfs()