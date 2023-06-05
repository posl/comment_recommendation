def dfs(v, p, c):
    color = 1
    for u in G[v]:
        if u == p:
            continue
        if color == c:
            color += 1
        ans[u] = color
        dfs(u, v, color)
        color += 1
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = [0] * N
ans[0] = 1
dfs(0, -1, 1)
print(max(ans))
for i in range(N - 1):
    print(ans[i + 1])
