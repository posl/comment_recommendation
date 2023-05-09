def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    # グラフの作成
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # 各頂点の深さを求める
    depth = [-1] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for w in G[v]:
            if depth[w] == -1:
                depth[w] = depth[v] + 1
                stack.append(w)
    # 各頂点の親を求める
    parent = [-1] * N
    stack = [0]
    while stack:
        v = stack.pop()
        for w in G[v]:
            if parent[w] == -1:
                parent[w] = v
                stack.append(w)
    # 各クエリについて答える
    for c, d in CD:
        c -= 1
        d -= 1
        if depth[c] < depth[d]:
            c, d = d, c
        while depth[c] > depth[d]:
            c = parent[c]
        while c != d:
            c = parent[c]
            d = parent[d]
        if depth[c] % 2 == 0:
            print("Town")
        else:
            print("Road")

if __name__ == '__main__':
    main()