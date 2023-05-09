def main():
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    print('Yes' if (A_x - D_x) * (B_y - D_y) - (A_y - D_y) * (B_x - D_x) > 0 and (B_x - A_x) * (C_y - A_y) - (B_y - A_y) * (C_x - A_x) > 0 and (C_x - B_x) * (D_y - B_y) - (C_y - B_y) * (D_x - B_x) > 0 and (D_x - C_x) * (A_y - C_y) - (D_y - C_y) * (A_x - C_x) > 0 else 'No')

if __name__ == '__main__':
    main()