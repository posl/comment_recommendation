def dfs(node, color, color_id):
    color[node] = color_id
    for edge in graph[node]:
        if color[edge[0]] == -1:
            dfs(edge[0], color, color_id ^ edge[1])
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w % 2))
    graph[v - 1].append((u - 1, w % 2))
color = [-1] * N
dfs(0, color, 0)
print(*color, sep="\n")

if __name__ == '__main__':
    dfs()