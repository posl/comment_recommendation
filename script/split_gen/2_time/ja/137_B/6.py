def get_black_stone(K, X):
    # 黒で塗られている石が置かれている可能性のある座標をすべて、小さい順に出力してください。
    # ここに処理を書き加えてください
    for i in range(-K+1, K):
        print(X+i, end = " ")
