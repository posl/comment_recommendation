def main():
    import sys
    from collections import deque
    N, X, Y = map(int, sys.stdin.readline().split())
    X -= 1
    Y -= 1
    graph = [[] for i in range(N)]
    for i in range(N-1):
        U, V = map(int, sys.stdin.readline().split())
        U -= 1
        V -= 1
        graph[U].append(V)
        graph[V].append(U)
    #print(graph)
    #print(X, Y)
    #print(graph[X])
    #print(graph[Y])
    #print(graph)
    dist = [-1]*N
    dist[X] = 0
    q = deque([X])
    while q:
        now = q.popleft()
        for next in graph[now]:
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                q.append(next)
    #print(dist)
    ans = [0]*N
    for i in range(N):
        ans[dist[i]] += 1
    ans[0] = -1
    print(*ans[1:])

if __name__ == '__main__':
    main()