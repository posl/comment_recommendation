def main():
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    # AB
    AB_x = B_x - A_x
    AB_y = B_y - A_y
    # BC
    BC_x = C_x - B_x
    BC_y = C_y - B_y
    # CD
    CD_x = D_x - C_x
    CD_y = D_y - C_y
    # DA
    DA_x = A_x - D_x
    DA_y = A_y - D_y
    AB_CD = AB_x * CD_y - AB_y * CD_x
    BC_DA = BC_x * DA_y - BC_y * DA_x
    if AB_CD * BC_DA >= 0:
        print('Yes')
    else:
        print('No')
