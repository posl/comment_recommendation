def dfs(v, c):
    color[v] = c
    for i in range(len(edge[v])):
        if color[edge[v][i]] == -1:
            dfs(edge[v][i], c ^ w[v][i])
n = int(input())
edge = [[] for i in range(n)]
w = [[] for i in range(n)]
color = [-1 for i in range(n)]
for i in range(n - 1):
    u, v, weight = map(int, input().split())
    edge[u - 1].append(v - 1)
    edge[v - 1].append(u - 1)
    w[u - 1].append(weight % 2)
    w[v - 1].append(weight % 2)
dfs(0, 0)
for i in range(n):
    print(color[i])

if __name__ == '__main__':
    dfs()