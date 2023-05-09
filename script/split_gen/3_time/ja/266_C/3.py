def main():
    import sys
    input = sys.stdin.readline
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    #四角形の４頂点の座標をリストに格納
    A = [A_x, A_y]
    B = [B_x, B_y]
    C = [C_x, C_y]
    D = [D_x, D_y]
    #４頂点の座標を時計回りに格納
    square = [A, B, C, D]
    #４頂点の座標から、AB, BC, CD, DAのベクトルを計算
    AB = [square[1][0] - square[0][0], square[1][1] - square[0][1]]
    BC = [square[2][0] - square[1][0], square[2][1] - square[1][1]]
    CD = [square[3][0] - square[2][0], square[3][1] - square[2][1]]
    DA = [square[0][0] - square[3][0], square[0][1] - square[3][1]]
    #AB, BC, CD, DAのベクトルから、外積を計算
    AB_BC = AB[0] * BC[1] - AB[1] * BC[0]
    BC_CD = BC[0] * CD[1] - BC[1] * CD[0]
    CD_DA = CD[0] * DA[1] - CD[1] * DA[0]
    DA_AB = DA[0] * AB[1] - DA[1] * AB[0]
    #外積が全て正の場合、凸である
    if AB_BC > 0 and BC_CD > 0 and CD_DA > 0 and DA_AB > 0:
        print("Yes")
    else:
        print("No")
