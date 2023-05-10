def main():
    N, X, Y = map(int, input().split())
    X, Y = X-1, Y-1
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    from collections import deque
    def bfs(graph, start):
        dist = [-1] * N
        dist[start] = 0
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for nv in graph[v]:
                if dist[nv] != -1:
                    continue
                dist[nv] = dist[v] + 1
                queue.append(nv)
        return dist
    dist = bfs(graph, X)
    print(dist[Y])
    return
main()

if __name__ == '__main__':
    main()