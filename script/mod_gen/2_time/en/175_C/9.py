def main():
    X, K, D = map(int, input().split())
    #X:現在の位置
    #K:移動回数
    #D:移動距離
    #Xが負の値の場合、正の値に変換する
    if X < 0:
        X = -X
    #XがDの倍数になるまで、Dを引く
    if X % D == 0:
        pass
    else:
        X = X - (X // D) * D
    #XがKの倍数になるまで、Dを引く
    if X % D == 0:
        pass
    else:
        X = X - (X // D) * D
    #XがKの倍数になるまで、Dを引く
    if X % D == 0:
        pass
    else:
        X = X - (X // D) * D
    #XがKの倍数になるまで、Dを引く
    if X % D == 0:
        pass
    else:
        X = X - (X // D) * D
    #XがKの倍数になるまで、Dを引く
    if X % D == 0:
        pass
    else:
        X = X - (X // D) * D
    #XがKの倍数になるまで、Dを引く
    if X % D == 0:
        pass
    else:
        X = X - (X // D) * D
    #XがKの倍数になるまで、Dを引く
    if X % D == 0:
        pass
    else:
        X = X - (X // D) * D
    #XがKの倍数になるまで、Dを引く
    if X % D == 0:
        pass
    else:
        X = X - (X // D) * D
    #XがKの倍数になるまで、Dを引く
    if X % D == 0:
        pass
    else:
        X = X - (X

if __name__ == '__main__':
    main()