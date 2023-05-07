def main():
    N = int(input())
    # 0,0 からの移動回数
    cnt = 0
    # 現在地
    now = (0,0)
    while True:
        # 今いるマスの数字
        num = now[0] * now[1]
        # 今いるマスの数字が N 以上ならば、そこに移動する
        if num >= N:
            break
        # 今いるマスの数字が N より小さいならば、右に移動するか下に移動するかを決める
        else:
            # 今いるマスの数字が 0 ならば、右に移動する
            if num == 0:
                now = (now[0] + 1, now[1])
            # 今いるマスの数字が 0 でないならば、右に移動するか下に移動するかを決める
            else:
                # 右に移動したときのマスの数字
                num_r = now[0] * (now[1] + 1)
                # 下に移動したときのマスの数字
                num_d = (now[0] + 1) * now[1]
                # 右に移動したときのマスの数字が N 以上ならば、下に移動する
                if num_r >= N:
                    now = (now[0], now[1] + 1)
                # 右に移動したときのマスの数字が N より小さいならば、下に移動したときのマスの数字が N 以上ならば、右に移動する
                elif num_d >= N:
                    now = (now[0] + 1, now[1])
                # 右に移動したときのマスの数字と下に移動したときのマスの数字が N より小さいならば、どちらに移動してもよい
                else:
                    # 右に移動したときのマスの数字が下
