def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
    # BFS
    visited = [False] * N
    visited[X] = True
    queue = [(X, 0)]
    while queue:
        v, d = queue.pop(0)
        if v == Y:
            print(d // 2)
            return
        for nv in edges[v]:
            if not visited[nv]:
                visited[nv] = True
                queue.append((nv, d + 1))
main()

if __name__ == '__main__':
    main()