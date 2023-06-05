def dfs(v, p, c):
    color = 1
    for i in range(len(g[v])):
        if g[v][i] == p:
            continue
        if color == c:
            color += 1
        ans[i] = color
        dfs(g[v][i], v, color)
        color += 1
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
ans = [0] * (n - 1)
dfs(0, -1, -1)
print(max(ans))
for i in range(n - 1):
    print(ans[i])

if __name__ == '__main__':
    dfs()