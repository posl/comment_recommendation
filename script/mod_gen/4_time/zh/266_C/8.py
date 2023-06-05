def main():
    # input
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    # process
    # A_x = 0
    # A_y = 0
    # B_x = 1
    # B_y = 0
    # C_x = 1
    # C_y = 1
    # D_x = 0
    # D_y = 1
    # A_x = 0
    # A_y = 0
    # B_x = 1
    # B_y = 1
    # C_x = -1
    # C_y = 0
    # D_x = 1
    # D_y = -1
    AB_x = B_x - A_x
    AB_y = B_y - A_y
    BC_x = C_x - B_x
    BC_y = C_y - B_y
    CD_x = D_x - C_x
    CD_y = D_y - C_y
    DA_x = A_x - D_x
    DA_y = A_y - D_y
    if AB_x * BC_y - AB_y * BC_x > 0 and BC_x * CD_y - BC_y * CD_x > 0 and CD_x * DA_y - CD_y * DA_x > 0 and DA_x * AB_y - DA_y * AB_x > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()