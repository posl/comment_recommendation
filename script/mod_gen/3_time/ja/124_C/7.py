def main():
    S = input()
    N = len(S)
    # 左から見ていく
    left = 0
    # 右から見ていく
    right = N - 1
    # 左から見ていくときの塗り替え回数
    left_count = 0
    # 右から見ていくときの塗り替え回数
    right_count = 0
    # 左から見ていくときの現在の色
    left_color = S[left]
    # 右から見ていくときの現在の色
    right_color = S[right]
    while left < right:
        # 左から見ていくときの現在の色と右から見ていくときの現在の色が同じ場合
        if left_color == right_color:
            # 左から見ていくときの塗り替え回数が右から見ていくときの塗り替え回数より多い場合
            if left_count > right_count:
                # 右から見ていくときの現在の色を反転させる
                right_color = '0' if right_color == '1' else '1'
                # 右から見ていくときの塗り替え回数をインクリメント
                right_count += 1
            # 左から見ていくときの塗り替え回数が右から見ていくときの塗り替え回数より少ない場合
            else:
                # 左から見ていくときの現在の色を反転させる
                left_color = '0' if left_color == '1' else '1'
                # 左から見ていくときの塗り替え回数をインクリメント
                left_count += 1
        # 左から見ていくときの現在の色と右から見ていくときの現在の色が違う場合

if __name__ == '__main__':
    main()