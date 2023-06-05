def dfs(i, color):
    global G, visited, colors
    visited[i] = True
    colors[i] = color
    for j in G[i]:
        if visited[j]:
            if colors[j] == color:
                return False
        else:
            if not dfs(j, 1 - color):
                return False
    return True
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
visited = [False] * n
colors = [-1] * n
ans = 0
for i in range(n):
    if not visited[i]:
        if dfs(i, 0):
            b = colors.count(0)
            w = colors.count(1)
            ans += b * (b - 1) // 2 + w * (w - 1) // 2
        else:
            ans = -1
            break
print(ans)

if __name__ == '__main__':
    dfs()