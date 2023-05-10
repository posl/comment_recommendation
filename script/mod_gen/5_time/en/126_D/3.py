def dfs(x, c):
    color[x] = c
    for y, w in edge[x]:
        if color[y] == -1:
            dfs(y, c ^ w)
n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append((v, w % 2))
    edge[v].append((u, w % 2))
color = [-1] * n
dfs(0, 0)
print(*color, sep='\n')

if __name__ == '__main__':
    dfs()