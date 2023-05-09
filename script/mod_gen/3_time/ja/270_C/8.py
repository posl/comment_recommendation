def main():
    N, X, Y = map(int, input().split())
    edges = []
    for _ in range(N - 1):
        edges.append(list(map(int, input().split())))
    print(edges)
    # print(N, X, Y)
    # print(edges)
    # return
    # 木の構造を作る
    # 隣接リストで表現する
    # 木の構造を作る
    # 隣接リストで表現する
    tree = [[] for _ in range(N + 1)]
    for e in edges:
        tree[e[0]].append(e[1])
        tree[e[1]].append(e[0])
    print(tree)
    # return
    # 頂点Xから頂点Yへの単純パスを求める
    # 頂点Xから頂点Yへの単純パスを求める
    # BFSで探索する
    # 頂点Xからの距離を求める
    # 頂点Yからの距離を求める
    # 頂点Xから頂点Yへの単純パスを求める
    # 頂点Xから頂点Yへの単純パスを求める
    # BFSで探索する
    # 頂点Xからの距離を求める
    # 頂点Yからの距離を求める
    # 頂点Xから頂点Yへの単純パスを求める
    # 頂点Xから頂点Yへの単純パスを求める
    # BFSで探索する
    # 頂点Xからの距離を求める
    # 頂点Yからの距離を求める
    # 頂点Xから頂点Yへの単純パスを求める
    # 頂点Xから頂点Yへの単

if __name__ == '__main__':
    main()