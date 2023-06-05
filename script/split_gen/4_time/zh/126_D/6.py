def dfs(v, c):
    color[v] = c
    for i in range(len(edge[v])):
        e = edge[v][i]
        if color[e] == -1:
            dfs(e, c^cost[v][i])
n = int(input())
edge = [[] for _ in range(n)]
cost = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)
    cost[u-1].append(w%2)
    cost[v-1].append(w%2)
color = [-1]*n
dfs(0, 0)
for c in color:
    print(c)
