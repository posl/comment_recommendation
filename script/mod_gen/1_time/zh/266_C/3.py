def is_convex_polygon(A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y):
    angle_A = (B_x-A_x)*(D_y-A_y)-(B_y-A_y)*(D_x-A_x)
    angle_B = (C_x-B_x)*(A_y-B_y)-(C_y-B_y)*(A_x-B_x)
    angle_C = (D_x-C_x)*(B_y-C_y)-(D_y-C_y)*(B_x-C_x)
    angle_D = (A_x-D_x)*(C_y-D_y)-(A_y-D_y)*(C_x-D_x)
    if angle_A>0 and angle_B>0 and angle_C>0 and angle_D>0:
        return 'Yes'
    elif angle_A<0 and angle_B<0 and angle_C<0 and angle_D<0:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    is_convex_polygon()