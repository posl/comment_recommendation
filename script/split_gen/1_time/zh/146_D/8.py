def dfs(v, p, c):
    color[c] = True
    col = 1
    for nv in G[v]:
        if nv == p:
            continue
        while color[col]:
            col += 1
        ans[nv] = col
        dfs(nv, v, col)
        col += 1
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = [0 for _ in range(N)]
color = [False for _ in range(N)]
ans[0] = 1
dfs(0, -1, 1)
print(max(ans))
for c in ans:
    print(c)
