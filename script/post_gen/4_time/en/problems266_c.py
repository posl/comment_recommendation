Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    dx, dy = map(int, input().split())
    if ((dx - ax) * (by - ay) - (bx - ax) * (dy - ay) > 0) and ((dx - bx) * (cy - by) - (cx - bx) * (dy - by) > 0) and ((dx - cx) * (ay - cy) - (ax - cx) * (dy - cy) > 0) and ((dx - dx) * (ay - dy) - (ax - dx) * (dy - dy) > 0):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    dx, dy = map(int, input().split())
    if (bx-ax)*(cy-ay)-(cx-ax)*(by-ay) > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())

    if (x2 - x1) * (y3 - y2) == (x3 - x2) * (y2 - y1) and (x2 - x1) * (y4 - y3) == (x4 - x3) * (y3 - y2) and (x2 - x1) * (y4 - y1) == (x4 - x1) * (y2 - y1):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def problem():
    A_x,A_y = map(int,input().split())
    B_x,B_y = map(int,input().split())
    C_x,C_y = map(int,input().split())
    D_x,D_y = map(int,input().split())
    AB_x = B_x - A_x
    AB_y = B_y - A_y
    BC_x = C_x - B_x
    BC_y = C_y - B_y
    CD_x = D_x - C_x
    CD_y = D_y - C_y
    DA_x = A_x - D_x
    DA_y = A_y - D_y
    AB = AB_x * BC_y - AB_y * BC_x
    BC = BC_x * CD_y - BC_y * CD_x
    CD = CD_x * DA_y - CD_y * DA_x
    DA = DA_x * AB_y - DA_y * AB_x
    if AB >= 0 and BC >= 0 and CD >= 0 and DA >= 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
  A_x,A_y = map(int,input().split())
  B_x,B_y = map(int,input().split())
  C_x,C_y = map(int,input().split())
  D_x,D_y = map(int,input().split())
  AB_x = B_x - A_x
  AB_y = B_y - A_y
  BC_x = C_x - B_x
  BC_y = C_y - B_y
  CD_x = D_x - C_x
  CD_y = D_y - C_y
  DA_x = A_x - D_x
  DA_y = A_y - D_y
  AB = AB_x * BC_y - AB_y * BC_x
  BC = BC_x * CD_y - BC_y * CD_x
  CD = CD_x * DA_y - CD_y * DA_x
  DA = DA_x * AB_y - DA_y * AB_x
  if AB * BC * CD * DA > 0:
    print('Yes')
  else:
    print('No')

=======
Suggestion 6

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

=======
Suggestion 7

def main():
    # your code goes here
    A_x,A_y = map(int,input().split())
    B_x,B_y = map(int,input().split())
    C_x,C_y = map(int,input().split())
    D_x,D_y = map(int,input().split())
    B_x = B_x - A_x
    B_y = B_y - A_y
    C_x = C_x - A_x
    C_y = C_y - A_y
    D_x = D_x - A_x
    D_y = D_y - A_y
    if B_x * C_y - B_y * C_x > 0 and B_x * D_y - B_y * D_x > 0 and C_x * D_y - C_y * D_x > 0:
        print("Yes")
    elif B_x * C_y - B_y * C_x < 0 and B_x * D_y - B_y * D_x < 0 and C_x * D_y - C_y * D_x < 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # get input
    Ax,Ay = map(int, input().split())
    Bx,By = map(int, input().split())
    Cx,Cy = map(int, input().split())
    Dx,Dy = map(int, input().split())

    # check convex
    if (Ax-Bx)*(Cy-Dy)-(Ay-By)*(Cx-Dx) > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def convex(a,b,c,d):
    if (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])>0:
        if (b[0]-a[0])*(d[1]-b[1])-(b[1]-a[1])*(d[0]-b[0])>0:
            if (d[0]-c[0])*(a[1]-d[1])-(d[1]-c[1])*(a[0]-d[0])>0:
                if (d[0]-c[0])*(b[1]-d[1])-(d[1]-c[1])*(b[0]-d[0])>0:
                    return 'Yes'
    return 'No'

a,b,c,d = [],[],[],[]
a.append(list(map(int,input().split())))
b.append(list(map(int,input().split())))
c.append(list(map(int,input().split())))
d.append(list(map(int,input().split())))
print(convex(a[0],b[0],c[0],d[0]))

=======
Suggestion 10

def get_input():
    points = []
    for i in range(4):
        points.append(list(map(int, input().split())))
    return points
