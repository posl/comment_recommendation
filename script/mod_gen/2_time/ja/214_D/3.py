def main():
    N = int(input())
    path = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        path[u - 1].append((v - 1, w))
        path[v - 1].append((u - 1, w))
    visited = [False] * N
    visited[0] = True
    stack = [(0, 0)]
    while stack:
        u, w = stack.pop()
        for v, w2 in path[u]:
            if visited[v]:
                continue
            visited[v] = True
            stack.append((v, w + w2))
    print(sum(w for w in visited) * (sum(visited) - 1))

if __name__ == '__main__':
    main()