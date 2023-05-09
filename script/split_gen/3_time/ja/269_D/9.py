def main():
    n = int(input())
    # 連結成分の数
    ans = 0
    # 各マスの白黒
    color = {}
    # 各連結成分の根
    root = {}
    # 各連結成分の要素数
    size = {}
    # 連結成分の根のリスト
    roots = []
    # 連結成分の要素数のリスト
    sizes = []
    # 連結成分の根を求める
    def find(x):
        if root[x] == x:
            return x
        else:
            root[x] = find(root[x])
            return root[x]
    # 連結成分を併合する
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        root[y] = x
        size[x] += size[y]
    # マスの白黒を入力
    for i in range(n):
        x, y = map(int, input().split())
        color[(x, y)] = 1
    # 各マスについて
    for x, y in color:
        # 連結成分の根を求める
        r = find((x, y))
        # 連結成分の根が未登録なら
        if r not in root:
            # 連結成分の根を登録
            root[r] = r
            # 連結成分の要素数を登録
            size[r] = 1
            # 連結成分の根のリストに追加
            roots.append(r)
            # 連結成分の要素数のリストに追加
            sizes.append(1)
            # 連結成分の数を増やす
            ans += 1
        # 連結成分の根が登録済みなら
        else:
            #
