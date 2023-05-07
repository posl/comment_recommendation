def main():
    A_x,A_y = map(int,input().split())
    B_x,B_y = map(int,input().split())
    C_x,C_y = map(int,input().split())
    D_x,D_y = map(int,input().split())
    if (A_x - C_x) * (B_y - C_y) - (A_y - C_y) * (B_x - C_x) == 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()