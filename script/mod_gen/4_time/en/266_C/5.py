def is_convex(A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y):
    A_x = int(A_x)
    A_y = int(A_y)
    B_x = int(B_x)
    B_y = int(B_y)
    C_x = int(C_x)
    C_y = int(C_y)
    D_x = int(D_x)
    D_y = int(D_y)
    if (B_x-A_x)*(C_y-A_y) - (B_y-A_y)*(C_x-A_x) > 0:
        if (D_x-B_x)*(A_y-B_y) - (D_y-B_y)*(A_x-B_x) > 0:
            if (C_x-D_x)*(B_y-D_y) - (C_y-D_y)*(B_x-D_x) > 0:
                if (A_x-C_x)*(D_y-C_y) - (A_y-C_y)*(D_x-C_x) > 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        if (D_x-B_x)*(A_y-B_y) - (D_y-B_y)*(A_x-B_x) > 0:
            if (C_x-D_x)*(B_y-D_y) - (C_y-D_y)*(B_x-D_x) > 0:
                if (A_x-C_x)*(D_y-C_y) - (A_y-C_y)*(D_x-C_x) > 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
input_line = input()
A_x,A_y = input_line.split()
input_line = input()
B_x,B_y = input_line.split()
input_line = input()
C_x,C_y = input_line.split()
input_line = input()
D_x,D_y = input_line.split()

if __name__ == '__main__':
    is_convex()