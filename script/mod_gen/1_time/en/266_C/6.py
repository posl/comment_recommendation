def is_convex(A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y):
    # A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y = map(int,input().split())
    # A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y = 0,0,1,0,1,1,0,1
    # A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y = 0,0,1,1,-1,0,1,-1
    A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y = A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y
    import math
    AB = math.sqrt((A_x-B_x)**2 + (A_y-B_y)**2)
    BC = math.sqrt((B_x-C_x)**2 + (B_y-C_y)**2)
    CD = math.sqrt((C_x-D_x)**2 + (C_y-D_y)**2)
    DA = math.sqrt((D_x-A_x)**2 + (D_y-A_y)**2)
    AC = math.sqrt((A_x-C_x)**2 + (A_y-C_y)**2)
    BD = math.sqrt((B_x-D_x)**2 + (B_y-D_y)**2)
    # print(AB,BC,CD,DA,AC,BD)
    AB_AC = math.acos(((A_x-B_x)*(A_x-C_x)+(A_y-B_y)*(A_y-C_y))/(AB*AC))
    BC_BD = math.acos(((B_x-C_x)*(B_x-D_x)+(B_y-C_y)*(B_y-D_y))/(BC*BD))
    CD_DA = math.acos(((C_x-D_x)*(C_x-A_x)+(C_y-D_y)*(C_y-A_y))/(CD*DA))
    DA_AB = math.acos(((D_x-A_x)*(D_x-B_x)+(D_y-A_y)*(D_y-B_y))/(DA*AB))
    # print(AB_AC,BC_BD,CD_DA,DA_AB)
    if AB_AC<math.pi and BC_BD<math.pi and CD_DA<math.pi and DA_AB<math.pi:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    is_convex()