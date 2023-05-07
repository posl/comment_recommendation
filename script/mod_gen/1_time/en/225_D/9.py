def main():
    N, Q = map(int, input().split())
    # 連結成分の根を管理するリスト
    # i番目の要素がiであれば、iは根
    # i番目の要素がjであれば、jがiの親
    root = [i for i in range(N+1)]
    # 連結成分のサイズを管理するリスト
    # 連結成分の根の要素に、連結成分のサイズを格納する
    size = [1]*(N+1)
    # 連結成分の根を求める
    def find(x):
        if x == root[x]:
            return x
        else:
            # 経路圧縮
            root[x] = find(root[x])
            return root[x]
    # 連結成分の併合
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        root[y] = x
        size[x] += size[y]
    # 連結成分のサイズを求める
    def get_size(x):
        return size[find(x)]
    # 連結成分の根を求める
    def get_root(x):
        return find(x)
    # クエリ処理
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            unite(query[1], query[2])
        elif query[0] == 2:
            unite(query[1], query[2])
        else:
            print(get_size(query[1]), end=' ')
            for i in range(1, N+1):
                if get_root(i) == get_root(query[1]):
                    print(i, end=' ')
            print()

if __name__ == '__main__':
    main()