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
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = [0] * N
dfs(0, -1, -1)
print(max(ans))
for i in ans:
    print(i)
