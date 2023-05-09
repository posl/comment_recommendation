def solve():
    import sys
    import math
    # 標準入力
    a, b = map(int, input().split())
    # 処理
    # 1回以上操作する場合
    if a >= b:
        # 1回目の操作を行うまでにかかる時間
        time = 1
        # 2回目以降の操作を行うまでにかかる時間
        time += b
        # 2回目以降の操作を行った後にかかる時間
        time += a / math.sqrt(b)
        # 結果出力
        print(time)
    # 1回も操作しない場合
    else:
        # 結果出力
        print(a)
