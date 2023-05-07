def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    color = [None] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u, w in G[v]:
            if color[u] is None:
                color[u] = color[v] ^ (w % 2)
                stack.append(u)
    print(*color, sep='
')

if __name__ == '__main__':
    main()