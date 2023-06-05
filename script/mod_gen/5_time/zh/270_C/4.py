def dfs(now,pre):
    global ans
    ans.append(now)
    for i in range(len(edge[now])):
        if edge[now][i] != pre:
            dfs(edge[now][i],now)
            ans.append(now)
    return
N,X,Y = map(int,input().split())
edge = [[] for i in range(N+1)]
for i in range(N-1):
    u,v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)
ans = []
dfs(X,-1)
ans.append(X)
ans.reverse()
dfs(Y,-1)
ans.append(Y)
ans = list(set(ans))
ans.sort()
print(*ans)

if __name__ == '__main__':
    dfs()