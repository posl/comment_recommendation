def main():
    N = int(input())
    # 1-indexed
    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))
    # 1-indexed
    color = [None] * (N + 1)
    color[1] = 0
    stack = [1]
    while stack:
        x = stack.pop()
        for y, w in G[x]:
            if color[y] is not None:
                continue
            color[y] = color[x] ^ (w % 2)
            stack.append(y)
    for i in range(1, N + 1):
        print(color[i])
