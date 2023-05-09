def dfs(v, c):
    color[v] = c
    for i in graph[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
color = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
ans = 0
for i in range(N):
    if color[i] == 0:
        if dfs(i, 1):
            cnt1 = color.count(1)
            cnt2 = color.count(-1)
            ans += cnt1 * cnt2
        else:
            ans += N * (N - 1) // 2
            break
print(ans)
