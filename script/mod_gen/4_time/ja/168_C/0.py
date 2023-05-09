def solve():
    import sys
    import math
    # 標準入力
    a, b, h, m = map(int, sys.stdin.readline().split())
    # 時針と分針の角度
    angle_h = 360 * (h % 12) / 12 + 360 * m / 12 / 60
    angle_m = 360 * m / 60
    # 時針と分針の角度の差
    angle_diff = abs(angle_h - angle_m)
    # 余弦定理
    # c^2 = a^2 + b^2 - 2ab * cos C
    # c = sqrt(a^2 + b^2 - 2ab * cos C)
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(angle_diff)))
    # 出力
    print(c)

if __name__ == '__main__':
    solve()