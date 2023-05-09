def main():
    # 木の頂点数
    N = int(input())
    # 木の頂点のリスト
    tree = [[] for _ in range(N+1)]
    # 木の辺のリスト
    edges = []
    # 木の頂点を受け取る
    for _ in range(N-1):
        u,v = map(int,input().split())
        tree[u].append(v)
        tree[v].append(u)
        edges.append([u,v])
    # 木の頂点のリストを辞書型に変換
    tree_dict = dict(zip(range(1,N+1),tree))
    # 木の頂点を受け取る
    X,Y = map(int,input().split())
    # 頂点Xから頂点Yへの単純パスを求める
    # 1. Xから頂点Yへのパスを求める
    path_X_Y = []
    # 1.1 Xから頂点Yへのパスを求める
    def search_path_X_Y(X,Y,path_X_Y):
        path_X_Y.append(X)
        if X == Y:
            return path_X_Y
        for node in tree_dict[X]:
            if node not in path_X_Y:
                path_X_Y = search_path_X_Y(node,Y,path_X_Y)
        return path_X_Y
    path_X_Y = search_path_X_Y(X,Y,path_X_Y)
    # 2. Xから頂点Yへの単純パスを求める
    # 2.1 Xから頂点Yへの単純パスを求める
    def search_simple_path_X_Y(path_X_Y):
        simple_path_X_Y = []
        for i in range(len(path_X_Y)-1):
            if path_X_Y[i+1] in tree_dict[path_X_Y[i]]:
                simple_path_X_Y.append(path_X_Y[i])
        simple_path_X_Y.append(path_X_Y[-1])
        return simple_path_X_Y
    simple_path_X_Y = search_simple_path_X_Y(path_X_Y)
    # 3. 頂点Xから頂点Yへの単純パ
