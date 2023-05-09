def main():
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    #四角形の面積が正ならば凸
    #四角形の面積が負ならば凹
    if (B_x - A_x) * (C_y - A_y) - (C_x - A_x) * (B_y - A_y) > 0:
        print("Yes")
    else:
        print("No")
