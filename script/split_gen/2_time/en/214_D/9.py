def main():
    import sys
    from collections import deque
    from heapq import heappush, heappop
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, w))
    # 1. 木の直径を求める
    def bfs(s):
        dist = [-1]*N
        que = deque([s])
        dist[s] = 0
        while que:
            v = que.popleft()
            for nv, w in G[v]:
                if dist[nv] != -1:
                    continue
                dist[nv] = dist[v] + w
                que.append(nv)
        return dist
    dist = bfs(0)
    max_v = max(range(N), key=lambda v: dist[v])
    dist = bfs(max_v)
    max_dist = max(dist)
    # 2. 木の直径の端点からの距離を求める
    dist = bfs(max_v)
    # 3. 木の直径の端点からの距離の和を求める
    ans = sum(dist)
    # 4. 木の直径の端点からの距離の和に、各辺の重みを足す
    for v in range(N):
        for nv, w in G[v]:
            if v > nv:
                continue
            ans += w*(dist[v] + dist[nv] - max_dist)
    print(ans)
