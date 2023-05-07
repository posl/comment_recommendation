def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 最大の角度
    max_angle = 0
    # すべての角度の和
    sum_angle = 0
    # すべての角度の和が360の倍数でない場合は、360の倍数になるように調整する
    for i in range(N):
        sum_angle += A[i]
        if sum_angle % 360 == 0:
            max_angle = 360
            break
    # すべての角度の和が360の倍数の場合は、最大の角度を求める
    if max_angle == 0:
        # すべての角度の和を360で割った余り
        mod = sum_angle % 360
        # 余りを引いた角度
        angle = 360 - mod
        # 余りを引いた角度が最大の角度
        max_angle = angle
    print(max_angle)
