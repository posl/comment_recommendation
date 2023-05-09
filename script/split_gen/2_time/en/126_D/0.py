def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    color = [None] * N
    color[0] = 0
    stack = [(0, 0)]
    while stack:
        v, c = stack.pop()
        for w, d in G[v]:
            if color[w] is None:
                color[w] = (c + d) % 2
                stack.append((w, color[w]))
    print(*color, sep='
')
