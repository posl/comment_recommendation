def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 連結成分の個数を管理する
    # 初期状態では全てが連結成分に分かれている
    root = [i for i in range(N + 1)]
    rank = [0 for i in range(N + 1)]
    size = [1 for i in range(N + 1)]
    # 連結成分の個数を返す
    def find(x):
        if root[x] == x:
            return x
        else:
            root[x] = find(root[x])
            return root[x]
    # xとyが同じ連結成分に属するか判定する
    def same(x, y):
        return find(x) == find(y)
    # xとyが属する連結成分を併合する
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            root[x] = y
            size[y] += size[x]
        else:
            root[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1
    # 残りの橋の個数を管理する
    # 初期状態では全ての橋が残っている
    remain = [1 for _ in range(M)]
    # 残りの橋の個数を返す
    def count(x):
        return remain[x]
    # 残りの橋の個数を1つ減らす
    def remove(x):
        remain[x] -= 1
    # 残りの橋の個数を返す
    def count(x):
        return remain[x]
    # 残りの橋の個数を1つ減らす
    def remove(x):
        remain[x] -= 1
    # 残

if __name__ == '__main__':
    main()