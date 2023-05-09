def main():
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    if ((B_x - A_x) * (C_y - A_y) - (B_y - A_y) * (C_x - A_x)) * ((B_x - A_x) * (D_y - A_y) - (B_y - A_y) * (D_x - A_x)) < 0:
        print("No")
    elif ((C_x - B_x) * (D_y - B_y) - (C_y - B_y) * (D_x - B_x)) * ((C_x - B_x) * (A_y - B_y) - (C_y - B_y) * (A_x - B_x)) < 0:
        print("No")
    elif ((D_x - C_x) * (A_y - C_y) - (D_y - C_y) * (A_x - C_x)) * ((D_x - C_x) * (B_y - C_y) - (D_y - C_y) * (B_x - C_x)) < 0:
        print("No")
    elif ((A_x - D_x) * (B_y - D_y) - (A_y - D_y) * (B_x - D_x)) * ((A_x - D_x) * (C_y - D_y) - (A_y - D_y) * (C_x - D_x)) < 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()