def is_convex_polygon(A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y):
    if (A_x * B_y + B_x * C_y + C_x * D_y + D_x * A_y - A_y * B_x - B_y * C_x - C_y * D_x - D_y * A_x) > 0:
        return 'Yes'
    else:
        return 'No'
