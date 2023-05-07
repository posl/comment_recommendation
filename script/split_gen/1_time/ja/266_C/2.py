def main():
    A_x,A_y = map(int,input().split())
    B_x,B_y = map(int,input().split())
    C_x,C_y = map(int,input().split())
    D_x,D_y = map(int,input().split())
    if (A_x - B_x) * (C_y - B_y) - (A_y - B_y) * (C_x - B_x) < 0:
        print("No")
    elif (B_x - C_x) * (D_y - C_y) - (B_y - C_y) * (D_x - C_x) < 0:
        print("No")
    elif (C_x - D_x) * (A_y - D_y) - (C_y - D_y) * (A_x - D_x) < 0:
        print("No")
    elif (D_x - A_x) * (B_y - A_y) - (D_y - A_y) * (B_x - A_x) < 0:
        print("No")
    else:
        print("Yes")
