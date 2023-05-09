def main():
    X, K, D = map(int, input().split())
    #Xの絶対値を取得
    X = abs(X)
    #K回の移動でXが0になる場合
    if X // D >= K:
        print(X - K * D)
        return
    #K回の移動でXが0にならない場合
    else:
        #Xが0になるまでの移動回数
        move_count = X // D
        #Xが0になるまでの移動で移動した距離
        move_distance = move_count * D
        #Xが0になるまでの移動で移動した距離を引いた値
        X = X - move_distance
        #Xが0になるまでに移動した回数が奇数回の場合
        if move_count % 2 == 1:
            print(abs(X - D))
            return
        #Xが0になるまでに移動した回数が偶数回の場合
        else:
            print(X)
            return
