def main():
    n, d = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(n)]
    # 区間の左端をキー、区間の右端を値とする辞書を作成
    # 区間の左端の値が大きい順にソート
    # 例：[[1, 2], [4, 7], [5, 9]] -> {1: 2, 4: 7, 5: 9}
    lr.sort(key=lambda x: x[0])
    lr = dict(lr)
    # 区間の左端をキー、区間の右端を値とする辞書を作成
    # 区間の右端の値が小さい順にソート
    # 例：[[1, 2], [4, 7], [5, 9]] -> {1: 2, 4: 7, 5: 9}
    lr2 = dict(sorted(lr.items(), key=lambda x: x[1]))
    # 区間の左端をキー、区間の右端を値とする辞書を作成
    # 区間の左端の値が大きい順にソート
    # 例：[[1, 2], [4, 7], [5, 9]] -> {1: 2, 4: 7, 5: 9}
    lr3 = dict(sorted(lr.items(), key=lambda x: x[0]))
    # 区間の左端をキー、区間の右端を値とする辞書を作成
    # 区間の右端の値が小さい順にソート
    # 例：[[1, 2], [4, 7], [5, 9]] -> {1: 2, 4: 7, 5: 9}
    lr4 = dict(sorted(lr.items(), key=lambda x: x[1]))
    # 破壊された壁の数
    destroyed = 0
    # パンチ
