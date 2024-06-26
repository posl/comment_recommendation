def dfs(v, c):
    color[v] = c
    for i in g[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
color = [0] * n
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            b = color.count(1)
            ans += b * (b - 1) // 2
            c = color.count(-1)
            ans += c * (c - 1) // 2
        else:
            print(0)
            exit()
print(ans)

if __name__ == '__main__':
    dfs()