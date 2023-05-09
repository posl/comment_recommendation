def main():
    X, K, D = map(int, input().split())
    # X:今の座標
    # K:移動回数
    # D:移動距離
    # 0に近づくほど絶対値が小さくなるので、
    # 0に近づくほど絶対値が小さくなるように移動するのが最適
    # Xが0より大きい場合はXをDで割った値の商が移動回数の最大値
    # Xが0より小さい場合はXをDで割った値の商の絶対値が移動回数の最大値
    # この最大値がKより大きい場合は、絶対値が0になる
    # この最大値がKより小さい場合は、絶対値が0にならず、
    # Xが0より大きい場合はXからKと最大値の差の2倍分のDを引いた値が絶対値が0になる
    # Xが0より小さい場合はXからKと最大値の差の2倍分のDを足した値が絶対値が0になる
    if X > 0:
        if X//D > K:
            print(X - K*D)
        else:
            if (K - X//D) % 2 == 0:
                print(X % D)
            else:
                print(abs(X % D - D))
    elif X < 0:
        if abs(X)//D > K:
            print(abs(X) - K*D)
        else:
            if (K - abs(X)//D) % 2 == 0:
                print(abs(X) % D)
            else:
                print(abs(abs(X) % D - D))
    else:
        print(K*D)
