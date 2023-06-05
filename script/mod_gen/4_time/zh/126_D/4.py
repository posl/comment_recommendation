def dfs(i, color):
    global ans
    visited[i] = 1
    ans[i] = color
    for j in range(len(graph[i])):
        if visited[graph[i][j][0]] == 0:
            if graph[i][j][1] % 2 == 0:
                dfs(graph[i][j][0], color)
            else:
                dfs(graph[i][j][0], 1 - color)
n = int(input())
graph = [[] for i in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append([v, w])
    graph[v].append([u, w])
visited = [0] * n
ans = [0] * n
dfs(0, 0)
for i in range(n):
    print(ans[i])

if __name__ == '__main__':
    dfs()