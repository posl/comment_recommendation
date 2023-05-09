def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))
    color = [0] * N
    stack = [(0, 0)]
    while stack:
        u, c = stack.pop()
        color[u] = c
        for v, w in graph[u]:
            if color[v] == 0:
                stack.append((v, c ^ (w % 2)))
    print(*color, sep='
')

if __name__ == '__main__':
    main()