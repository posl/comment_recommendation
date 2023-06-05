def is_convex_polygon(A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y):
    # write your code here
    angle_A = get_angle(A_x, A_y, B_x, B_y, C_x, C_y)
    angle_B = get_angle(B_x, B_y, C_x, C_y, D_x, D_y)
    angle_C = get_angle(C_x, C_y, D_x, D_y, A_x, A_y)
    angle_D = get_angle(D_x, D_y, A_x, A_y, B_x, B_y)
    if angle_A + angle_B + angle_C + angle_D == 360:
        return 'Yes'
    else:
        return 'No'
