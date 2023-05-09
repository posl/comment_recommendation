def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    colors = [-1 for _ in range(N)]
    colors[0] = 0
    dfs(graph, colors, 0)
    for color in colors:
        print(color)
