def main():
    N = int(input())
    # 木の隣接リスト
    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))
    # DFS
    # 0: 白
    # 1: 黒
    # -1: 未訪問
    colors = [-1] * N
    colors[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in tree[v]:
            if colors[nv] == -1:
                colors[nv] = (colors[v] + w) % 2
                stack.append(nv)
    for c in colors:
        print(c)

if __name__ == '__main__':
    main()