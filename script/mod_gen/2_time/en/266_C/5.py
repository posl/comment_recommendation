def main():
    # Step #1 - Create Input
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    # Step #2 - Create Logic
    AB = (B_x - A_x, B_y - A_y)
    BC = (C_x - B_x, C_y - B_y)
    CD = (D_x - C_x, D_y - C_y)
    DA = (A_x - D_x, A_y - D_y)
    # Step #3 - Create Output
    if AB[0]*BC[1] - AB[1]*BC[0] < 0:
        print("No")
    elif BC[0]*CD[1] - BC[1]*CD[0] < 0:
        print("No")
    elif CD[0]*DA[1] - CD[1]*DA[0] < 0:
        print("No")
    elif DA[0]*AB[1] - DA[1]*AB[0] < 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()