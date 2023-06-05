def main():
    Ax,Ay = map(int,input().split())
    Bx,By = map(int,input().split())
    Cx,Cy = map(int,input().split())
    Dx,Dy = map(int,input().split())
    if ((Bx-Ax)*(Cy-By)-(By-Ay)*(Cx-Bx))*((Cx-Bx)*(Dy-Cy)-(Cy-By)*(Dx-Cx))<0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()