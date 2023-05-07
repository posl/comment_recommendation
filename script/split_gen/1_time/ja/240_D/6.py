def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 筒の中にあるボールの個数
    ball_num = 0
    # 筒の中にあるボールの個数を記録するリスト
    ball_num_list = [0] * N
    # 筒の中にあるボールの個数の前回の値
    prev_ball_num = 0
    # 筒の中にあるボールの個数の前回の値を記録するリスト
    prev_ball_num_list = [0] * N
    # 筒の中にあるボールの個数を記録するリストのインデックス
    i = 0
    for a in A:
        # 筒の中にあるボールの個数の前回の値を記録するリストに記録
        prev_ball_num_list[i] = prev_ball_num
        # ボールの個数の前回の値を更新
        prev_ball_num = ball_num
        # ボールの個数を更新
        ball_num += 1
        # ボールの個数がボールに書かれた整数と同じならば
        if ball_num == a:
            # ボールの個数を 0 に更新
            ball_num = 0
        # 筒の中にあるボールの個数を記録するリストに記録
        ball_num_list[i] = ball_num
        # ボールの個数を記録するリストのインデックスを更新
        i += 1
    # 筒の中にあるボールの個数を記録するリストのインデックスを 0 にリセット
    i = 0
    for a in A:
        # 筒の中にあるボールの個数の前回の値を記録するリストの値を
