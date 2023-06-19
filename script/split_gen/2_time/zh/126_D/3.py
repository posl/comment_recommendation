def dfs(s, color):
    global ans
    ans[s] = color
    for t, w in G[s]:
        if ans[t] != -1:
            continue
        if w % 2 == 0:
            dfs(t, color)
        else:
            dfs(t, 1 - color)
    return
N = int(input())
G = [[] for i in range(N)]
ans = [-1 for i in range(N)]
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))
dfs(0, 0)
for i in range(N):
    print(ans[i])
