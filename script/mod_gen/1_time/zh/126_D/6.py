def dfs(node, color):
    global ans
    ans[node] = color
    for i in range(len(graph[node])):
        if ans[graph[node][i]] == -1:
            dfs(graph[node][i], color ^ cost[node][i])
n = int(input())
graph = [[] for _ in range(n)]
cost = [[] for _ in range(n)]
ans = [-1] * n
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
    cost[u].append(w % 2)
    cost[v].append(w % 2)
dfs(0, 0)
for i in range(n):
    print(ans[i])

if __name__ == '__main__':
    dfs()