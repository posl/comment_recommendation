def dfs(v):
    if visited[v]:
        return
    visited[v] = True
    for next_v in graph[v]:
        dfs(next_v)
    ans.append(v+1)
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
visited = [False] * N
ans = []
for i in range(N):
    dfs(i)
print('Yes')
for i in range(N-1):
    print(ans[i+1])

if __name__ == '__main__':
    dfs()