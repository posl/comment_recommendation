def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    visited = [False] * N
    visited[0] = True
    stack = [0]
    while stack:
        v = stack.pop()
        for u in graph[v]:
            if visited[u]:
                continue
            visited[u] = True
            stack.append(u)
    print('Yes' if all(visited) else 'No')
main()

if __name__ == '__main__':
    main()