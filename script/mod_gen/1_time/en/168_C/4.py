def main():
    a, b, h, m = map(int, input().split())
    # 12時間で360度回転するので、1時間で30度、1分で0.5度回転
    # 時針はh時間m分で回転するので、h*30+m*0.5度回転
    # 分針はm分で回転するので、m*6度回転
    # 時針と分針の角度差を求める
    d = abs((h*30+m*0.5)-(m*6))
    # 時針と分針の角度差が180度以上なら、360度から角度差を引く
    if d >= 180:
        d = 360-d
    # 角度差をラジアンに直す
    d = d / 180 * math.pi
    # 三角関数を使って、時針と分針の間の距離を求める
    print(math.sqrt(a**2+b**2-2*a*b*math.cos(d)))

if __name__ == '__main__':
    main()