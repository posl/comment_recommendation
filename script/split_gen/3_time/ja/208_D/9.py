def main():
    from collections import deque
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    INF = 10 ** 18
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dist[i][i] = 0
    for i in range(1, N + 1):
        q = deque()
        q.append(i)
        while q:
            v = q.popleft()
            for nv, c in graph[v]:
                if dist[i][nv] > dist[i][v] + c:
                    dist[i][nv] = dist[i][v] + c
                    q.append(nv)
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if dist[i][j] == dist[i][k] + dist[k][j]:
                    ans += dist[i][j]
                    break
    print(ans)
