def dfs(v, p, d):
    global ans
    ans += d
    for i in range(len(g[v])):
        if g[v][i][0] != p:
            dfs(g[v][i][0], v, max(d, g[v][i][1]))
n = int(input())
g = [[] for i in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    g[u - 1].append((v - 1, w))
    g[v - 1].append((u - 1, w))
ans = 0
dfs(0, -1, 0)
print(ans)

if __name__ == '__main__':
    dfs()