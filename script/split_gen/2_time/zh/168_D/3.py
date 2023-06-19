def dfs(now, pre):
    for i in G[now]:
        if i == pre:
            continue
        if vis[i] == 0:
            vis[i] = now
            dfs(i, now)
        else:
            if vis[now] == 0:
                vis[now] = i
                dfs(i, now)
N, M = map(int, input().split())
G = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
vis = [0] * (N+1)
vis[1] = -1
dfs(1, -1)
for i in range(1, N+1):
    if vis[i] == 0:
        print('No')
        exit()
print('Yes')
for i in range(2, N+1):
    print(vis[i])
