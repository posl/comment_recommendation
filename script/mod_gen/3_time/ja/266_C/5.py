def main():
    import sys
    input = sys.stdin.readline
    #入力
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    #凸判定
    if (B_x - A_x) * (C_y - A_y) - (C_x - A_x) * (B_y - A_y) > 0:
        if (C_x - B_x) * (D_y - B_y) - (D_x - B_x) * (C_y - B_y) > 0:
            if (D_x - C_x) * (A_y - C_y) - (A_x - C_x) * (D_y - C_y) > 0:
                if (A_x - D_x) * (B_y - D_y) - (B_x - D_x) * (A_y - D_y) > 0:
                    print("Yes")
                    return
    print("No")

if __name__ == '__main__':
    main()