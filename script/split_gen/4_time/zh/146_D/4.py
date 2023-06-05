def dfs(v, p, c):
    color = 1
    for i in G[v]:
        if i == p:
            continue
        if color == c:
            color += 1
        ans[i] = color
        dfs(i, v, color)
        color += 1
N = int(input())
G = [[] for _ in range(N)]
ans = [0] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
dfs(0, -1, -1)
print(max(ans))
for i in ans:
    print(i)
