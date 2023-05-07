def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    # 奇数番目の頂点は黒、偶数番目の頂点は白で塗る
    # 0: 白, 1: 黒
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for to, w in G[v]:
            if color[to] != -1:
                continue
            if w % 2 == 0:
                color[to] = color[v]
            else:
                color[to] = 1 - color[v]
            stack.append(to)
    for c in color:
        print(c)

if __name__ == '__main__':
    main()