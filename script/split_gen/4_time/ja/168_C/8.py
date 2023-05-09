def main():
    A, B, H, M = map(int, input().split())
    import math
    # 針の角度
    H_angle = 360 * H / 12 + 360 * M / 12 / 60
    M_angle = 360 * M / 60
    # 針の角度差
    angle = abs(H_angle - M_angle)
    # 余弦定理
    ans = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(math.radians(angle)))
    print(ans)
main()
