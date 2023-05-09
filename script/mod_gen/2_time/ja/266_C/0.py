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

if __name__ == '__main__':
    main()