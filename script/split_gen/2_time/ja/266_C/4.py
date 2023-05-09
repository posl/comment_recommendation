def main():
    import sys
    input = sys.stdin.readline
    A_x,A_y = map(int,input().split())
    B_x,B_y = map(int,input().split())
    C_x,C_y = map(int,input().split())
    D_x,D_y = map(int,input().split())
    if (A_x-A_y)*(B_x-B_y)+(A_x-A_y)*(C_x-C_y)+(B_x-B_y)*(D_x-D_y)+(C_x-C_y)*(D_x-D_y) < 0:
        print("Yes")
    else:
        print("No")
