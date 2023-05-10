def main():
    A_x,A_y = map(int, input().split())
    B_x,B_y = map(int, input().split())
    C_x,C_y = map(int, input().split())
    D_x,D_y = map(int, input().split())
    if ((B_x-A_x)*(C_y-A_y) - (B_y-A_y)*(C_x-A_x))*((B_x-A_x)*(D_y-A_y) - (B_y-A_y)*(D_x-A_x)) < 0:
        print('Yes')
    else:
        print('No')
