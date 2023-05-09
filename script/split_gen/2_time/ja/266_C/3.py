def main():
    Ax,Ay = map(int,input().split())
    Bx,By = map(int,input().split())
    Cx,Cy = map(int,input().split())
    Dx,Dy = map(int,input().split())
    if (Bx-Ax)*(Cy-Ay) == (By-Ay)*(Cx-Ax):
        print("No")
    else:
        print("Yes")
