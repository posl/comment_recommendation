def dfs(now, parent):
    global ans
    ans.append(now)
    for i in edge[now]:
        if i != parent:
            dfs(i, now)
            ans.append(now)
    return ans
N = int(input())
edge = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
for i in range(N):
    edge[i].sort()
ans = []
dfs(0, -1)
print(*[i + 1 for i in ans])
