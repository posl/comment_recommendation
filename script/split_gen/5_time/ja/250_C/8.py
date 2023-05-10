def main():
    # 標準入力から N, Q を取得する
    N, Q = map(int, input().split())
    # 標準入力から x を取得する
    x = [int(input()) for _ in range(Q)]
    # 1 から N までの数値を配列に格納する
    a = list(range(1, N + 1))
    # x の値が a の中で何番目にあるかを取得する
    for i in range(Q):
        index = a.index(x[i])
        # x の値が a の最後の要素だった場合
        if index == N - 1:
            # a の最後の要素と a の最後から 2 番目の要素を入れ替える
            a[index], a[index - 1] = a[index - 1], a[index]
        # x の値が a の最後の要素以外だった場合
        else:
            # a の x の値がある場所と a の x の値の次の要素を入れ替える
            a[index], a[index + 1] = a[index + 1], a[index]
    # 結果を出力する
    print(*a)
