def main():
    N, M = map(int, input().split())
    a = [0] * M
    b = [0] * M
    for i in range(M):
        a[i], b[i] = map(int, input().split())
    a = [x - 1 for x in a]
    b = [x - 1 for x in b]
    # 各ノードの親を記録する
    # つまり、各ノードの根を記録する
    parent = [-1] * N
    # ノードxの根を求める
    def root(x):
        # ノードxの親が存在しない場合は、xが根である
        if parent[x] < 0:
            return x
        # ノードxの親が存在する場合は、親の根を求める
        else:
            # 根を求めると同時に、xの親を根につなぎ直す
            parent[x] = root(parent[x])
            return parent[x]
    # ノードxとノードyの属する集合を併合する
    def unite(x, y):
        # ノードxとノードyの根を求める
        x = root(x)
        y = root(y)
        # ノードxとノードyの根が同じ場合は、何もしない
        if x == y:
            return
        # ノードxの根の方がノードyの根よりも大きい場合は、xとyを入れ替える
        if parent[x] > parent[y]:
            x, y = y, x
        # ノードxの根の子供にノードyの根を追加する
        parent[x] += parent[y]
        parent[y] = x
    # ノードxとノードyが同じ集合に属するかどうかを判定する
    def same(x, y):
        return root(x) == root(y)
    #

if __name__ == '__main__':
    main()