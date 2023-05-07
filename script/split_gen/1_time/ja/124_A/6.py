def main():
    # A, Bは入力
    A, B = map(int, input().split())
    # A, Bの大きい方をmax_numに代入
    max_num = max(A, B)
    # A, Bの小さい方をmin_numに代入
    min_num = min(A, B)
    # max_numの2回押す枚数をmax_num_doubleに代入
    max_num_double = max_num * 2
    # min_numの1回押す枚数をmin_num_singleに代入
    min_num_single = min_num
    # max_num_doubleとmin_num_singleの大きい方を出力
    print(max(max_num_double, min_num_single))
