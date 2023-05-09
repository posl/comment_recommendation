def main():
    a, b, h, m = map(int, input().split())
    # 時針の角度
    theta = 360 / 12 * h + 360 / 12 / 60 * m
    # 分針の角度
    phi = 360 / 60 * m
    # 2つの角度の差
    d = abs(theta - phi)
    # 2つの角度の差が180度以上なら、それを360度から引く
    if d >= 180:
        d = 360 - d
    # 2つの角度の差のラジアン
    rad = d * math.pi / 180
    # 2つの角度の差のラジアンを使って、針の長さを求める
    print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(rad)))
