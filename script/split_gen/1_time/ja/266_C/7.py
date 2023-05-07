def main():
    # A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y = map(int,input().split())
    A_x,A_y = map(int,input().split())
    B_x,B_y = map(int,input().split())
    C_x,C_y = map(int,input().split())
    D_x,D_y = map(int,input().split())
    A = [A_x,A_y]
    B = [B_x,B_y]
    C = [C_x,C_y]
    D = [D_x,D_y]
    # print(A,B,C,D)
    AB = [B_x-A_x,B_y-A_y]
    BC = [C_x-B_x,C_y-B_y]
    CD = [D_x-C_x,D_y-C_y]
    DA = [A_x-D_x,A_y-D_y]
    # print(AB,BC,CD,DA)
    if 0 < AB[0]*BC[1]-AB[1]*BC[0] < 0:
        print('No')
    elif 0 < BC[0]*CD[1]-BC[1]*CD[0] < 0:
        print('No')
    elif 0 < CD[0]*DA[1]-CD[1]*DA[0] < 0:
        print('No')
    elif 0 < DA[0]*AB[1]-DA[1]*AB[0] < 0:
        print('No')
    else:
        print('Yes')
