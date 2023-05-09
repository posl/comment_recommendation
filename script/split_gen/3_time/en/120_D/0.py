def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M)
    #print(A)
    #print(B)
    # 橋の破壊順を逆にする
    A.reverse()
    B.reverse()
    # 累積和を計算する
    # 累積和の初期値は、全ての橋を通れる状態
    # つまり、全ての島の親は同じで、同じグループに属している
    # そのため、累積和は、最初はNをM個分追加して、M個分引く
    # これで、最初のグループの数を計算できる
    # その後、各島の親を更新していく
    group = [N] * (M + 1)
    for i in range(M):
        group[i + 1] = group[i] + 1 - group[i + 1]
    #print(group)
    # 連結成分の個数
    # 連結成分の個数を数えるために、Union Findを使う
    # 連結成分の個数を数えるには、
    # 1. 連結成分の個数を数える
    # 2. 橋を破壊する
    # 3. 連結成分の個数を数える
    # 4. 2. 3. を繰り返す
    # という流れになる
    # 1. 連結成分の個数を数える
    # 連結成分の個数を数えるには、
    # 1.1. 最初は各島
