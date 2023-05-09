def main():
    import sys
    from collections import deque
    from heapq import heappush, heappop
    input = sys.stdin.readline
    N = int(input())
    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))
    q = deque()
    q.append(1)
    visited = [False] * (N + 1)
    visited[1] = True
    parent = [0] * (N + 1)
    while q:
        v = q.popleft()
        for u, w in G[v]:
            if visited[u]:
                continue
            parent[u] = v
            visited[u] = True
            q.append(u)
    dist = [0] * (N + 1)
    for i in range(2, N + 1):
        dist[i] = dist[parent[i]] + G[parent[i]][i]
    ans = 0
    for i in range(2, N + 1):
        ans += dist[i] * (N - dist[i])
    print(ans)
