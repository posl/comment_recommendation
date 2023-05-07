def main():
    #入力
    A_x, A_y = map(int,input().split())
    B_x, B_y = map(int,input().split())
    C_x, C_y = map(int,input().split())
    D_x, D_y = map(int,input().split())
    #処理
    if (B_x - A_x) * (C_y - B_y) - (B_y - A_y) * (C_x - B_x) >= 0 and (C_x - B_x) * (D_y - C_y) - (C_y - B_y) * (D_x - C_x) >= 0 and (D_x - C_x) * (A_y - D_y) - (D_y - C_y) * (A_x - D_x) >= 0 and (A_x - D_x) * (B_y - A_y) - (A_y - D_y) * (B_x - A_x) >= 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()