def main():
    A, B, H, M = map(int, input().split())
    #時針の角度
    theta = (H * 60 + M) * 360 / (12 * 60)
    #分針の角度
    phi = M * 360 / 60
    #時針と分針の角度差
    theta = abs(theta - phi)
    #時針と分針の角度差が180度以上なら、180度を引く
    if theta > 180:
        theta = 360 - theta
    #角度差をラジアンに変換
    theta = math.radians(theta)
    #cosθ = (A^2 + B^2 - C^2) / 2AB
    C = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta))
    print(C)

if __name__ == '__main__':
    main()