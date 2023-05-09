def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    # print(graph)
    # print(X, Y)
    from collections import deque
    q = deque()
    q.append((X, 0))
    visited = [-1] * N
    visited[X] = 0
    while q:
        v, d = q.popleft()
        for nv in graph[v]:
            if visited[nv] == -1:
                visited[nv] = d + 1
                q.append((nv, d + 1))
    # print(visited)
    ans = [0] * N
    for i in range(N):
        if i != X:
            ans[visited[i]] += 1
    print(*ans[1:], sep=" ")

if __name__ == '__main__':
    main()