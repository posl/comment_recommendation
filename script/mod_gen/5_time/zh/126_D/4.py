def dfs(u, c):
    color[u] = c
    for i in range(len(edge[u])):
        v = edge[u][i]
        if color[v] == -1:
            dfs(v, c ^ 1)
n = int(input())
edge = [[] for i in range(n)]
color = [-1] * n
for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w % 2 == 0:
        edge[u].append(v)
        edge[v].append(u)
dfs(0, 0)
for i in range(n):
    print(color[i])

if __name__ == '__main__':
    dfs()