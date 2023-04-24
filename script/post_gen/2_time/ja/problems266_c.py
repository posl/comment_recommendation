Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    # 2つのベクトルの外積が正ならば凸
    if (B_x - A_x) * (C_y - B_y) - (B_y - A_y) * (C_x - B_x) > 0:
        if (C_x - B_x) * (D_y - C_y) - (C_y - B_y) * (D_x - C_x) > 0:
            if (D_x - C_x) * (A_y - D_y) - (D_y - C_y) * (A_x - D_x) > 0:
                if (A_x - D_x) * (B_y - A_y) - (A_y - D_y) * (B_x - A_x) > 0:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 2

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

=======
Suggestion 3

def main():
    A_x,A_y = map(int,input().split())
    B_x,B_y = map(int,input().split())
    C_x,C_y = map(int,input().split())
    D_x,D_y = map(int,input().split())
    a = (B_x - A_x) * (C_y - A_y)
    b = (C_x - A_x) * (B_y - A_y)
    c = (C_x - B_x) * (D_y - B_y)
    d = (D_x - B_x) * (C_y - B_y)
    e = (D_x - C_x) * (A_y - C_y)
    f = (A_x - C_x) * (D_y - C_y)
    g = (A_x - D_x) * (B_y - D_y)
    h = (B_x - D_x) * (A_y - D_y)
    if a - b > 0 and c - d > 0 and e - f > 0 and g - h > 0:
        print("Yes")
    elif a - b < 0 and c - d < 0 and e - f < 0 and g - h < 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    Ax,Ay = map(int,input().split())
    Bx,By = map(int,input().split())
    Cx,Cy = map(int,input().split())
    Dx,Dy = map(int,input().split())
    if (Bx-Ax)*(Cy-Ay) == (By-Ay)*(Cx-Ax):
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    A_x,A_y = map(int,input().split())
    B_x,B_y = map(int,input().split())
    C_x,C_y = map(int,input().split())
    D_x,D_y = map(int,input().split())
    if (A_x-A_y)*(B_x-B_y)+(A_x-A_y)*(C_x-C_y)+(B_x-B_y)*(D_x-D_y)+(C_x-C_y)*(D_x-D_y) < 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    D = list(map(int,input().split()))
    if (A[0] - B[0]) * (C[1] - B[1]) - (A[1] - B[1]) * (C[0] - B[0]) > 0:
        print("No")
    elif (B[0] - C[0]) * (D[1] - C[1]) - (B[1] - C[1]) * (D[0] - C[0]) > 0:
        print("No")
    elif (C[0] - D[0]) * (A[1] - D[1]) - (C[1] - D[1]) * (A[0] - D[0]) > 0:
        print("No")
    elif (D[0] - A[0]) * (B[1] - A[1]) - (D[1] - A[1]) * (B[0] - A[0]) > 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    # 3点のなす角度を求める
    def angle(A, B, C):
        # 内積
        ab = (B[0]-A[0]) * (C[0]-B[0]) + (B[1]-A[1]) * (C[1]-B[1])
        # 外積
        ac = (B[0]-A[0]) * (C[1]-B[1]) - (B[1]-A[1]) * (C[0]-B[0])
        return np.arctan2(ac, ab) * 180 / np.pi

    # 3点のなす角度の和を求める
    angle_sum = angle(A, B, C) + angle(B, C, D) + angle(C, D, A) + angle(D, A, B)

    if angle_sum == 360:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    # 座標を入力
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    D = [int(i) for i in input().split()]

    # 座標の差を計算
    AB = [B[0] - A[0], B[1] - A[1]]
    BC = [C[0] - B[0], C[1] - B[1]]
    CD = [D[0] - C[0], D[1] - C[1]]
    DA = [A[0] - D[0], A[1] - D[1]]

    # 座標の差の外積を計算
    cross_AB_BC = AB[0] * BC[1] - AB[1] * BC[0]
    cross_BC_CD = BC[0] * CD[1] - BC[1] * CD[0]
    cross_CD_DA = CD[0] * DA[1] - CD[1] * DA[0]
    cross_DA_AB = DA[0] * AB[1] - DA[1] * AB[0]

    # 外積の積が負なら凹
    if cross_AB_BC * cross_BC_CD * cross_CD_DA * cross_DA_AB < 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline
    from itertools import permutations
    #入力
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    D = list(map(int,input().split()))
    #頂点の座標をリストにまとめる
    P = [A,B,C,D]
    #頂点の座標の組み合わせを全て試す
    for i in permutations(P,4):
        #角度を求める
        #A-B-C
        a = (i[1][0]-i[0][0])*(i[2][0]-i[1][0])+(i[1][1]-i[0][1])*(i[2][1]-i[1][1])
        b = ((i[1][0]-i[0][0])**2+(i[1][1]-i[0][1])**2)**0.5
        c = ((i[2][0]-i[1][0])**2+(i[2][1]-i[1][1])**2)**0.5
        ABC = abs(a)/(b*c)
        #B-C-D
        a = (i[2][0]-i[1][0])*(i[3][0]-i[2][0])+(i[2][1]-i[1][1])*(i[3][1]-i[2][1])
        b = ((i[2][0]-i[1][0])**2+(i[2][1]-i[1][1])**2)**0.5
        c = ((i[3][0]-i[2][0])**2+(i[3][1]-i[2][1])**2)**0.5
        BCD = abs(a)/(b*c)
        #C-D-A
        a = (i[3][0]-i[2][0])*(i[0][0]-i[3][0])+(i[3][1]-i[2][1])*(i[0][1]-i[3][1])
        b = ((i[3][0]-i[2][0])**2+(
