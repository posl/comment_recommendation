def main():
    import sys
    from heapq import heappop, heappush
    from itertools import count
    from collections import defaultdict
    def dijkstra(start, graph):
        dist = defaultdict(lambda: float('inf'))
        dist[start] = 0
        q = [(0, start)]
        while q:
            d, v = heappop(q)
            if d > dist[v]:
                continue
            for u, c in graph[v]:
                if dist[u] > d + c:
                    dist[u] = d + c
                    heappush(q, (d + c, u))
        return dist
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = defaultdict(list)
    for i in range(M):
        a, b, c = map(int, input().split())
        G[a].append((b, c))
    ans = 0
    for i in range(1, N + 1):
        dist = dijkstra(i, G)
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if dist[j] != float('inf') and dist[j] <= dist[k]:
                    ans += dist[j]
    print(ans)

if __name__ == '__main__':
    main()