def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # 人の体重の最大値
    maxW = max(W)
    # 人の体重の最小値
    minW = min(W)
    # 体重の最大値と最小値を使って、体重の増減の幅を決める
    dW = maxW - minW
    # 体重の増減の幅の最大値
    maxdW = 10**9
    # 体重の増減の幅の最小値
    mindW = 1
    # 体重の増減の幅の中央値
    midW = (maxdW + mindW) // 2
    # 体重の増減の幅が最大値になるまで繰り返す
    while dW != maxdW:
        # 体重の増減の幅の中央値の値で判定する
        # 体重の増減の幅の中央値が小さいと、体重の増減の幅を大きくする
        if judge(S, W, midW):
            mindW = midW
        # 体重の増減の幅の中央値が大きいと、体重の増減の幅を小さくする
        else:
            maxdW = midW
        # 体重の増減の幅の中央値を更新する
        midW = (maxdW + mindW) // 2
        # 体重の増減の幅の最大値と最小値の差を更新する
        dW = maxdW - mindW
    # 体重の増減の幅の中央値を出力する
    print(midW)
