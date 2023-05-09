def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 1周の長さ
    len = K
    # 総移動距離
    total = 0
    # 1周の移動距離
    len_move = 0
    # 1周の移動距離を計算
    for i in range(N-1):
        len_move += A[i+1] - A[i]
    # 1周の移動距離が最短の場合
    if len_move < len:
        len = len_move
    # 1周の移動距離が最短でない場合
    else:
        # 1周の移動距離の半分を計算
        len_move_half = len_move // 2
        # 1周の移動距離が偶数の場合
        if len_move % 2 == 0:
            # 1周の移動距離の半分が最短の場合
            if len_move_half < len:
                len = len_move_half
        # 1周の移動距離が奇数の場合
        else:
            # 1周の移動距離の半分が最短の場合
            if len_move_half < len:
                len = len_move_half
            # 1周の移動距離の半分+1が最短の場合
            elif len_move_half + 1 < len:
                len = len_move_half + 1
    # 1周の移動距離が最短の場合
    if len == len_move:
        # 総移動距離を計算
        for i in range(N-1):
            total += A[i+1] - A[i]
    # 1周の移動距離が最短でない場合
    else:
        # 総移動距離を計算
        for i in range(N

if __name__ == '__main__':
    main()