def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    tree = [[] for _ in range(N)]
    for u, v, w in edges:
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        u = stack.pop()
        for v, w in tree[u]:
            if color[v] != -1:
                continue
            color[v] = color[u] ^ (w % 2)
            stack.append(v)
    print(*color, sep='
')
main()
