def dfs(v, c):
    color[v] = c
    for i in G[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True
N, M, K = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
color = [0] * N
for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            print(0)
            exit()
ans = [0] * N
for i in range(N):
    ans[i] = color.count(color[i])
for i in range(N):
    ans[i] -= len(G[i]) + 1
print(*ans)
