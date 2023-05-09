def main():
    N = int(input())
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        tree[u-1].append((v-1, w))
        tree[v-1].append((u-1, w))
    Q = [(0, 0)]
    color = [-1] * N
    color[0] = 0
    while Q:
        v, c = Q.pop()
        for u, w in tree[v]:
            if color[u] != -1:
                continue
            color[u] = (c + w) % 2
            Q.append((u, color[u]))
    print(*color, sep="\n")
