def dfs(x):
    if vis[x]: return
    vis[x] = 1
    for y in G[x]:
        if vis[y]: continue
        dfs(y)
    ans.append(x)
n,m = map(int,input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
vis = [0]*(n+1)
ans = []
for i in range(1,n+1):
    if vis[i]: continue
    dfs(i)
ans = ans[::-1]
vis = [0]*(n+1)
ans2 = []
for i in ans:
    if vis[i]: continue
    ans2.append(i)
    vis[i] = 1
    for j in G[i]:
        vis[j] = 1
print("Yes")
for i in ans2:
    print(i)
