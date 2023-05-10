def main():
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    #Determine the angle of the quadrilateral at A
    Angle_A = (B_x-A_x)*(C_y-A_y) - (B_y-A_y)*(C_x-A_x)
    #Determine the angle of the quadrilateral at B
    Angle_B = (C_x-B_x)*(D_y-B_y) - (C_y-B_y)*(D_x-B_x)
    #Determine the angle of the quadrilateral at C
    Angle_C = (D_x-C_x)*(A_y-C_y) - (D_y-C_y)*(A_x-C_x)
    #Determine the angle of the quadrilateral at D
    Angle_D = (A_x-D_x)*(B_y-D_y) - (A_y-D_y)*(B_x-D_x)
    #Determine whether the quadrilateral is convex
    if Angle_A > 0 and Angle_B > 0 and Angle_C > 0 and Angle_D > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()