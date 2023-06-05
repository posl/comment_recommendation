def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    # print(G)
    # BFS
    from collections import deque
    def bfs(s):
        dist = [-1] * N
        dist[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for u, w in G[v]:
                if dist[u] == -1:
                    dist[u] = dist[v] + w
                    q.append(u)
        return dist
    dist = bfs(0)
    # print(dist)
    max_dist = max(dist)
    max_idx = dist.index(max_dist)
    dist = bfs(max_idx)
    # print(dist)
    print(sum(dist))
main()
