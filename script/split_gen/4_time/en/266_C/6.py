def main():
    # your code goes here
    A_x,A_y = map(int,input().split())
    B_x,B_y = map(int,input().split())
    C_x,C_y = map(int,input().split())
    D_x,D_y = map(int,input().split())
    B_x = B_x - A_x
    B_y = B_y - A_y
    C_x = C_x - A_x
    C_y = C_y - A_y
    D_x = D_x - A_x
    D_y = D_y - A_y
    if B_x * C_y - B_y * C_x > 0 and B_x * D_y - B_y * D_x > 0 and C_x * D_y - C_y * D_x > 0:
        print("Yes")
    elif B_x * C_y - B_y * C_x < 0 and B_x * D_y - B_y * D_x < 0 and C_x * D_y - C_y * D_x < 0:
        print("Yes")
    else:
        print("No")
