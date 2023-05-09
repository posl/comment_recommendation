def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)
    dist = [N] * N
    dist[X] = 0
    queue = [X]
    while queue:
        v = queue.pop(0)
        for w in edges[v]:
            if dist[w] > dist[v] + 1:
                dist[w] = dist[v] + 1
                queue.append(w)
    print(dist[Y])

if __name__ == '__main__':
    main()