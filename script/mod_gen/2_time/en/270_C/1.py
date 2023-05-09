def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    stack = [X]
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if dist[w] != -1:
                continue
            dist[w] = dist[v] + 1
            stack.append(w)
    print(*dist)

if __name__ == '__main__':
    main()