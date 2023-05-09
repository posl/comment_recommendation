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

if __name__ == '__main__':
    main()