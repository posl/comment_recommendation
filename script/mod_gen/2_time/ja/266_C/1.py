def main():
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    # 三角形の面積を求める
    # 三角形の面積: S = 1/2 * |(x1*y2+x2*y3+x3*y1)-(x1*y3+x2*y1+x3*y2)|
    s1 = abs((A_x*B_y+B_x*C_y+C_x*A_y)-(A_x*C_y+B_x*A_y+C_x*B_y))/2
    s2 = abs((A_x*C_y+B_x*D_y+D_x*A_y)-(A_x*D_y+B_x*A_y+D_x*C_y))/2
    s3 = abs((A_x*D_y+B_x*C_y+C_x*A_y)-(A_x*C_y+B_x*D_y+C_x*A_y))/2
    s4 = abs((C_x*D_y+D_x*B_y+B_x*C_y)-(C_x*B_y+D_x*C_y+B_x*D_y))/2
    # 三角形の面積が全て0なら凸ではない
    if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()