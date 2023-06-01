Synthesizing 10/10 solutions

=======
Suggestion 1

def cross_product(a,b):
	return a[0]*b[1]-a[1]*b[0]

=======
Suggestion 2

def is_convex_polygon(A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y):
    if (A_x * B_y + B_x * C_y + C_x * D_y + D_x * A_y - A_y * B_x - B_y * C_x - C_y * D_x - D_y * A_x) > 0:
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 3

def main():
    x = []
    y = []
    for i in range(4):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    if (x[1]-x[0])*(y[2]-y[1]) - (y[1]-y[0])*(x[2]-x[1]) > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

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

=======
Suggestion 5

def cross_product(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1

=======
Suggestion 6

def is_convex(a, b, c, d):
    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]) > 0 and \
           (c[0] - b[0]) * (d[1] - c[1]) - (c[1] - b[1]) * (d[0] - c[0]) > 0 and \
           (d[0] - c[0]) * (a[1] - d[1]) - (d[1] - c[1]) * (a[0] - d[0]) > 0 and \
           (a[0] - d[0]) * (b[1] - a[1]) - (a[1] - d[1]) * (b[0] - a[0]) > 0 or \
           (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]) < 0 and \
           (c[0] - b[0]) * (d[1] - c[1]) - (c[1] - b[1]) * (d[0] - c[0]) < 0 and \
           (d[0] - c[0]) * (a[1] - d[1]) - (d[1] - c[1]) * (a[0] - d[0]) < 0 and \
           (a[0] - d[0]) * (b[1] - a[1]) - (a[1] - d[1]) * (b[0] - a[0]) < 0

=======
Suggestion 7

def main():
    Ax,Ay = map(int,input().split())
    Bx,By = map(int,input().split())
    Cx,Cy = map(int,input().split())
    Dx,Dy = map(int,input().split())
    if ((Bx-Ax)*(Cy-By)-(By-Ay)*(Cx-Bx))*((Cx-Bx)*(Dy-Cy)-(Cy-By)*(Dx-Cx))<0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def cross_product(ax, ay, bx, by):
    return ax*by - ay*bx

=======
Suggestion 9

def is_convex(A, B, C, D):
    # 通过向量叉积判断两个向量的方向
    # A->B, B->C, C->D, D->A
    AB = [B[0] - A[0], B[1] - A[1]]
    BC = [C[0] - B[0], C[1] - B[1]]
    CD = [D[0] - C[0], D[1] - C[1]]
    DA = [A[0] - D[0], A[1] - D[1]]
    # 判断AB与BC的叉积方向是否相同
    if AB[0] * BC[1] - AB[1] * BC[0] < 0:
        return False
    # 判断BC与CD的叉积方向是否相同
    if BC[0] * CD[1] - BC[1] * CD[0] < 0:
        return False
    # 判断CD与DA的叉积方向是否相同
    if CD[0] * DA[1] - CD[1] * DA[0] < 0:
        return False
    # 判断DA与AB的叉积方向是否相同
    if DA[0] * AB[1] - DA[1] * AB[0] < 0:
        return False
    return True

=======
Suggestion 10

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
