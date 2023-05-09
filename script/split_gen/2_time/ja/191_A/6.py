def main():
    # 標準入力を取得
    V, T, S, D = map(int,input().split())
    # 高橋君が投げたボールが消える時間を計算
    disappear_time = V * T
    # 高橋君が投げたボールが消える距離を計算
    disappear_distance = V * S
    # 高橋君が投げたボールが消える時間と距離を比較
    if D < disappear_time or D > disappear_distance:
        print('Yes')
    else:
        print('No')
