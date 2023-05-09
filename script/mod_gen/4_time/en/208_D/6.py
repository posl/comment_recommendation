def main():
    import sys
    from collections import deque
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist = [float("inf")] * (N + 1)
            dist[i] = 0
            q = deque([i])
            while q:
                v = q.popleft()
                for nv, c in graph[v]:
                    if dist[nv] > dist[v] + c:
                        dist[nv] = dist[v] + c
                        q.append(nv)
            ans += dist[j]
    print(ans)

if __name__ == '__main__':
    main()