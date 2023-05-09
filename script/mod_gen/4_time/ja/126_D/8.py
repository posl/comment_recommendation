def dfs(now, color, g, ans):
    ans[now] = color
    for next in g[now]:
        if ans[next] == -1:
            dfs(next, 1 - color, g, ans)
N = int(input())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w % 2 == 0:
        g[u].append(v)
        g[v].append(u)
ans = [-1] * N
dfs(0, 0, g, ans)
for i in range(N):
    print(ans[i])

if __name__ == '__main__':
    dfs()