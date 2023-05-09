def main():
    import sys
    from collections import deque
    N = int(sys.stdin.readline())
    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(N - 1)]
    graph = [[] for _ in range(N + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    #print(graph)
    q = deque([1])
    dist = [0] * (N + 1)
    visited = [False] * (N + 1)
    visited[1] = True
    while q:
        u = q.popleft()
        for v, w in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + w
                q.append(v)
    #print(dist)
    ans = 0
    for u, v, w in edges:
        ans += w * (dist[u] + dist[v] + w)
    print(ans)
