def main():
    A, B, H, M = map(int, input().split())
    # 1時間を60分とする
    # 1分を360度とする
    # 1時間を360度とする
    # 1時間を12時間とする
    # 1時間を360度とする
    # 1時間を12時間とする
    # 時針の角度
    theta_H = (360/12) * H + (360/12/60) * M
    # 分針の角度
    theta_M = (360/60) * M
    # 2本の針の角度の差
    theta = abs(theta_H - theta_M)
    # 2本の針の角度の差が180度以上なら、360度から引く
    if theta >= 180:
        theta = 360 - theta
    # 2本の針の角度の差をラジアンに変換
    theta = math.radians(theta)
    # 2本の針の角度の差から、2本の針の端点の距離を求める
    print(math.sqrt(A**2 + B**2 - 2*A*B*math.cos(theta)))

if __name__ == '__main__':
    main()