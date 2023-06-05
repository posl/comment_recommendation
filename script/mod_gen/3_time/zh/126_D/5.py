def dfs(cur, col):
    color[cur] = col
    for i in range(len(graph[cur])):
        if color[graph[cur][i]] == -1:
            dfs(graph[cur][i], col ^ cost[cur][i])
N = int(input())
graph = [[] for i in range(N)]
cost = [[] for i in range(N)]
color = [-1 for i in range(N)]
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
    cost[u].append(w % 2)
    cost[v].append(w % 2)
dfs(0, 0)
for i in range(N):
    print(color[i])

if __name__ == '__main__':
    dfs()