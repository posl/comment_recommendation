def dfs(v, c):
    color[v] = c
    for i in G[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
color = [0] * N
ans = 0
for i in range(N):
    if color[i] == 0:
        if dfs(i, 1):
            cnt1 = color.count(1)
            cnt2 = color.count(-1)
            ans += cnt1 * cnt2
        else:
            ans = -1
            break
print(ans)
