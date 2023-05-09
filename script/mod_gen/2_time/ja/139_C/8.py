def main():
    N = int(input())
    H = list(map(int, input().split()))
    # 最大移動回数
    max_move = 0
    # 今までの移動回数
    move = 0
    # 最後のマスまで移動
    for i in range(N-1):
        # 次のマスの高さが現在のマスの高さ以下のとき
        if H[i] >= H[i+1]:
            # 今までの移動回数をインクリメント
            move += 1
        # 次のマスの高さが現在のマスの高さより高いとき
        else:
            # 今までの移動回数をリセット
            move = 0
        # 最大移動回数を更新
        if move > max_move:
            max_move = move
    # 最大移動回数を出力
    print(max_move)

if __name__ == '__main__':
    main()