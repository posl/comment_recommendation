def main():
    #入力
    X, K, D = map(int, input().split())
    #絶対値を取る
    X = abs(X)
    #移動回数が移動距離を超えている場合
    if K > X // D:
        #移動回数から移動距離を引いた回数だけ移動距離を減らす
        K -= X // D
        #移動距離を減らす
        X -= X // D * D
        #移動回数が奇数の場合
        if K % 2 == 1:
            #移動距離を減らす
            X -= D
    #移動回数が移動距離を超えていない場合
    else:
        #移動距離を減らす
        X -= K * D
    #絶対値を取る
    X = abs(X)
    #出力
    print(X)

if __name__ == '__main__':
    main()