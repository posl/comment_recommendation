def dfs(i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)
N,M=map(int,input().split())
graph=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
visited=[False]*N
ans=0
for i in range(N):
    if not visited[i]:
        dfs(i)
        ans+=1
print(ans-1)

if __name__ == '__main__':
    dfs()