def main():
    N = int(input())
    X = []
    Y = []
    P = []
    for i in range(N):
        x, y, p = list(map(int, input().split()))
        X.append(x)
        Y.append(y)
        P.append(p)
    # 二次元配列を作成
    # 0: 到達できるかどうか
    # 1: そのジャンプ台に到達するために必要な訓練回数
    # 2: そのジャンプ台に到達するために必要な訓練回数の最大値
    # 3: そのジャンプ台に到達するために必要な訓練回数の最小値
    # 4: そのジャンプ台に到達するために必要な訓練回数の最大値を超えるかどうか
    # 5: そのジャンプ台に到達するために必要な訓練回数の最小値を下回るかどうか
    # 6: そのジャンプ台に到達するために必要な訓練回数の最大値を超えるジャンプ台のリスト
    # 7: そのジャンプ台に到達するために必要な訓練回数の最小値を下回るジャンプ台のリスト
    # 8: そのジャンプ台に到達するために必要な訓練回数の最大値を超えるジャンプ台のリストの数
    # 9: そのジャンプ台に到達するために必要な訓練回数の最小値を下回るジャンプ台のリストの数
    # 10: そのジャンプ台に到達するために必要な訓

if __name__ == '__main__':
    main()