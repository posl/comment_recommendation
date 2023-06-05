def dfs(u, c):
    color[u] = c
    for v, w in g[u]:
        if color[v] == -1:
            dfs(v, c ^ w)
N = int(input())
g = [[] for _ in range(N)]
color = [-1] * N
for _ in range(N - 1):
    x, y, w = map(int, input().split())
    g[x - 1].append((y - 1, w % 2))
    g[y - 1].append((x - 1, w % 2))
dfs(0, 0)
for c in color:
    print(c)

if __name__ == '__main__':
    dfs()