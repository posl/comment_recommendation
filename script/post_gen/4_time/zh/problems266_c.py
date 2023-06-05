Synthesizing 10/10 solutions

=======
Suggestion 1

def judgeConvex(A,B,C,D):
    #AB,BC,CD,DA
    if (B[0]-A[0])*(C[1]-B[1])-(C[0]-B[0])*(B[1]-A[1])<0:
        return False
    if (C[0]-B[0])*(D[1]-C[1])-(D[0]-C[0])*(C[1]-B[1])<0:
        return False
    if (D[0]-C[0])*(A[1]-D[1])-(A[0]-D[0])*(D[1]-C[1])<0:
        return False
    if (A[0]-D[0])*(B[1]-A[1])-(B[0]-A[0])*(A[1]-D[1])<0:
        return False
    return True

=======
Suggestion 2

def is_convex(x1, y1, x2, y2, x3, y3, x4, y4):
    # 1. 任意两边的叉积同号
    # 2. 任意两条边不相交
    # 3. 任意两条边不平行
    # 4. 任意三个点不共线
    # 5. 任意三个点不同
    # 6. 任意两条边不重合
    # 7. 任意两条边不平行
    # 8. 任意两条边不相交
    # 9. 任意两个点不重合
    # 10. 任意两条边不重合
    # 11. 任意两条边不平行
    # 12. 任意两条边不相交
    # 13. 任意两个点不重合
    # 14. 任意两条边不重合
    # 15. 任意两条边不平行
    # 16. 任意两条边不相交
    # 17. 任意两个点不重合
    # 18. 任意两条边不重合
    # 19. 任意两条边不平行
    # 20. 任意两条边不相交
    # 21. 任意两个点不重合
    # 22. 任意两条边不重合
    # 23. 任意两条边不平行
    # 24. 任意两条边不相交
    # 25. 任意两个点不重合
    # 26. 任意两条边不重合
    # 27. 任意两条边不平行
    # 28. 任意两条边不相交
    # 29. 任意两个点不重合
    # 30. 任意两条边不重合

=======
Suggestion 3

def check_convex(a,b,c,d):
    #计算向量ab和bc的叉积
    x1=b[0]-a[0]
    y1=b[1]-a[1]
    x2=c[0]-b[0]
    y2=c[1]-b[1]
    z1=x1*y2-x2*y1
    #计算向量bc和cd的叉积
    x1=c[0]-b[0]
    y1=c[1]-b[1]
    x2=d[0]-c[0]
    y2=d[1]-c[1]
    z2=x1*y2-x2*y1
    #计算向量cd和da的叉积
    x1=d[0]-c[0]
    y1=d[1]-c[1]
    x2=a[0]-d[0]
    y2=a[1]-d[1]
    z3=x1*y2-x2*y1
    #计算向量da和ab的叉积
    x1=a[0]-d[0]
    y1=a[1]-d[1]
    x2=b[0]-a[0]
    y2=b[1]-a[1]
    z4=x1*y2-x2*y1
    #如果z1 z2 z3 z4都是正数或者都是负数，那么就是凸四边形
    if (z1>0 and z2>0 and z3>0 and z4>0) or (z1<0 and z2<0 and z3<0 and z4<0):
        return True
    else:
        return False

=======
Suggestion 4

def check_convex(a, b, c, d):
    # 1. check cross product
    # 2. check inner product
    # 3. check area
    # 4. check angle

    # 1. check cross product
    def cross_product(x1, y1, x2, y2):
        return x1 * y2 - x2 * y1

    def inner_product(x1, y1, x2, y2):
        return x1 * x2 + y1 * y2

    def area(x1, y1, x2, y2, x3, y3):
        return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

    def angle(x1, y1, x2, y2, x3, y3):
        return inner_product(x2 - x1, y2 - y1, x3 - x1, y3 - y1)

    # 1. check cross product
    a1 = cross_product(b[0] - a[0], b[1] - a[1], c[0] - a[0], c[1] - a[1])
    a2 = cross_product(b[0] - a[0], b[1] - a[1], d[0] - a[0], d[1] - a[1])
    b1 = cross_product(d[0] - c[0], d[1] - c[1], a[0] - c[0], a[1] - c[1])
    b2 = cross_product(d[0] - c[0], d[1] - c[1], b[0] - c[0], b[1] - c[1])

    if a1 * a2 < 0 and b1 * b2 < 0:
        return False

    # 2. check inner product
    if inner_product(b[0] - a[0], b[1] - a[1], d[0] - c[0], d[1] - c[1]) > 0:
        return False
    if inner_product(c[0] - b[0], c[1] - b[1], a[0

=======
Suggestion 5

def isConvex(A,B,C,D):
    #计算向量
    AB = (B[0]-A[0],B[1]-A[1])
    BC = (C[0]-B[0],C[1]-B[1])
    CD = (D[0]-C[0],D[1]-C[1])
    DA = (A[0]-D[0],A[1]-D[1])
    #计算向量叉乘
    ABxBC = AB[0]*BC[1]-AB[1]*BC[0]
    BCxCD = BC[0]*CD[1]-BC[1]*CD[0]
    CDxDA = CD[0]*DA[1]-CD[1]*DA[0]
    DAxAB = DA[0]*AB[1]-DA[1]*AB[0]
    #判断正负
    if ABxBC*BCxCD>0 and BCxCD*CDxDA>0 and CDxDA*DAxAB>0:
        return True
    else:
        return False

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    ax,ay = map(int,input().split())
    bx,by = map(int,input().split())
    cx,cy = map(int,input().split())
    dx,dy = map(int,input().split())
    if (ax-dx)*(by-dy) - (ay-dy)*(bx-dx) > 0 and \
        (bx-ax)*(cy-ay) - (by-ay)*(cx-ax) > 0 and \
        (cx-bx)*(dy-by) - (cy-by)*(dx-bx) > 0 and \
        (dx-cx)*(ay-cy) - (dy-cy)*(ax-cx) > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def isConvex(a,b,c,d):
    #print(a,b,c,d)
    #print(a[0],b[0],c[0],d[0])
    #print(a[1],b[1],c[1],d[1])
    #print((b[0]-a[0])*(c[1]-b[1]))
    #print((b[1]-a[1])*(c[0]-b[0]))
    #print((b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0]))
    #print((c[0]-b[0])*(d[1]-c[1]))
    #print((c[1]-b[1])*(d[0]-c[0]))
    #print((c[0]-b[0])*(d[1]-c[1])-(c[1]-b[1])*(d[0]-c[0]))
    #print((d[0]-c[0])*(a[1]-d[1]))
    #print((d[1]-c[1])*(a[0]-d[0]))
    #print((d[0]-c[0])*(a[1]-d[1])-(d[1]-c[1])*(a[0]-d[0]))
    #print((a[0]-d[0])*(b[1]-a[1]))
    #print((a[1]-d[1])*(b[0]-a[0]))
    #print((a[0]-d[0])*(b[1]-a[1])-(a[1]-d[1])*(b[0]-a[0]))
    if (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])>0:
        if (c[0]-b[0])*(d[1]-c[1])-(c[1]-b[1])*(d[0]-c[0])>0:
            if (d[0]-c[0])*(a[1]-d[1])-(d[1]-c[1])*(a[0]-d[0])>0

=======
Suggestion 9

def main():
    # input
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())

    # process
    # A_x = 0
    # A_y = 0
    # B_x = 1
    # B_y = 0
    # C_x = 1
    # C_y = 1
    # D_x = 0
    # D_y = 1
    # A_x = 0
    # A_y = 0
    # B_x = 1
    # B_y = 1
    # C_x = -1
    # C_y = 0
    # D_x = 1
    # D_y = -1
    AB_x = B_x - A_x
    AB_y = B_y - A_y
    BC_x = C_x - B_x
    BC_y = C_y - B_y
    CD_x = D_x - C_x
    CD_y = D_y - C_y
    DA_x = A_x - D_x
    DA_y = A_y - D_y
    if AB_x * BC_y - AB_y * BC_x > 0 and BC_x * CD_y - BC_y * CD_x > 0 and CD_x * DA_y - CD_y * DA_x > 0 and DA_x * AB_y - DA_y * AB_x > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def isConvex(a, b, c, d):
    # a, b, c, d: (x, y)
    # return: True if the quadrangle is convex, False otherwise
    # WRITE ME!
    a = (b[0] - a[0], b[1] - a[1])
    b = (c[0] - b[0], c[1] - b[1])
    c = (d[0] - c[0], d[1] - c[1])
    d = (a[0] - d[0], a[1] - d[1])
    a = a[0] * b[1] - a[1] * b[0]
    b = b[0] * c[1] - b[1] * c[0]
    c = c[0] * d[1] - c[1] * d[0]
    d = d[0] * a[1] - d[1] * a[0]
    return a * b > 0 and b * c > 0 and c * d > 0
