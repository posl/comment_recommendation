def main():
    import sys
    from operator import itemgetter
    from itertools import accumulate
    from bisect import bisect_left
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    # 始点と終点をそれぞれ切り出す
    a, b = map(list, zip(*ab))
    # 終点を昇順にソート
    b.sort()
    # 終点を累積和に変換
    # 例えば [1, 2, 3] なら [1, 3, 6]
    b = list(accumulate(b))
    # 各始点について、終点の累積和から始点より小さい最大の終点のインデックスを求める
    # 例えば [1, 2, 3] なら [0, 0, 1]
    # 例えば [1, 3, 6] なら [0, 0, 1]
    c = [bisect_left(b, x) for x in a]
    # 0 ～ N-1 のインデックスについて、終点の累積和からそのインデックスより小さい最大の終点のインデックスを引く
    # 例えば [0, 0, 1] なら [1, 1, 0]
    # 例えば [0, 0, 1] なら [1, 1, 0]
    d = [b[x] - x for x in c]
    # 0 ～ N-1 のインデックスについて、終点の累積和からそのインデックスより小さい最大の終点のインデックスを引く
    # 例えば [1, 1, 0] なら [1, 1, 0]
    # 例えば [1, 1, 0] なら [1, 1, 0]
