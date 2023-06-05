def dfs(v, p, c):
    color[c] = True
    ans[v] = c
    k = 1
    for i in range(len(g[v])):
        if g[v][i] == p: continue
        while color[k]: k += 1
        dfs(g[v][i], v, k)
n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
ans = [0] * (n+1)
color = [False] * (n+1)
dfs(1, 0, 0)
print(max(ans))
for i in range(1, n):
    print(ans[i])

if __name__ == '__main__':
    dfs()