def main():
    A_x,A_y = map(int,input().split())
    B_x,B_y = map(int,input().split())
    C_x,C_y = map(int,input().split())
    D_x,D_y = map(int,input().split())
    a = (B_x - A_x) * (C_y - A_y)
    b = (C_x - A_x) * (B_y - A_y)
    c = (C_x - B_x) * (D_y - B_y)
    d = (D_x - B_x) * (C_y - B_y)
    e = (D_x - C_x) * (A_y - C_y)
    f = (A_x - C_x) * (D_y - C_y)
    g = (A_x - D_x) * (B_y - D_y)
    h = (B_x - D_x) * (A_y - D_y)
    if a - b > 0 and c - d > 0 and e - f > 0 and g - h > 0:
        print("Yes")
    elif a - b < 0 and c - d < 0 and e - f < 0 and g - h < 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()