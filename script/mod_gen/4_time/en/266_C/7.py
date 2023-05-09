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

if __name__ == '__main__':
    main()