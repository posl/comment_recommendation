def dfs(node, color):
    global colors, nodes, edges
    colors[node] = color
    for edge in edges[node]:
        if colors[edge[0]] == -1:
            dfs(edge[0], color ^ edge[1])
n = int(input())
nodes = []
for i in range(n):
    nodes.append([])
edges = {}
for i in range(n - 1):
    u, v, w = map(int, input().split())
    nodes[u - 1].append([v - 1, w % 2])
    nodes[v - 1].append([u - 1, w % 2])
    edges[i] = [u - 1, v - 1, w % 2]
colors = [-1 for i in range(n)]
dfs(0, 0)
for color in colors:
    print(color)

if __name__ == '__main__':
    dfs()