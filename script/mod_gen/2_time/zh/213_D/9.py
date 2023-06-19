def dfs(x):
    global ans
    ans.append(x)
    visited[x] = True
    for i in range(len(g[x])):
        if not visited[g[x][i]]:
            dfs(g[x][i])
            ans.append(x)
    return
n = int(input())
g = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(1,n+1):
    g[i].sort()
visited = [False] * (n+1)
ans = []
dfs(1)
print(*ans)

if __name__ == '__main__':
    dfs()