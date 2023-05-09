def main():
    N, Q = map(int, input().split())
    # 木の構築
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # 各頂点のカウンターの値
    C = [0] * N
    # 各操作
    for _ in range(Q):
        p, x = map(int, input().split())
        C[p-1] += x
    # 根から順にカウンターの値を伝搬
    q = [0]
    while q:
        v = q.pop()
        for w in G[v]:
            if C[w] == 0:
                C[w] = C[v]
                q.append(w)
    # 出力
    print(" ".join(map(str, C)))

if __name__ == '__main__':
    main()