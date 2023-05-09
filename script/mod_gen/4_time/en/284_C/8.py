def dfs(v):
    visited[v] = True
    for i in range(n):
        if not visited[i] and graph[v][i]:
            dfs(i)
n,m = map(int, input().split())
graph = [[False] * n for i in range(n)]
for i in range(m):
    u,v = map(int, input().split())
    graph[u-1][v-1] = True
    graph[v-1][u-1] = True
visited = [False] * n
count = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)

if __name__ == '__main__':
    dfs()