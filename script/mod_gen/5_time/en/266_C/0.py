def main():
    Ax, Ay = map(int, input().split())
    Bx, By = map(int, input().split())
    Cx, Cy = map(int, input().split())
    Dx, Dy = map(int, input().split())
    A = (Bx - Ax) * (Cy - Ay) - (By - Ay) * (Cx - Ax)
    B = (Cx - Bx) * (Dy - By) - (Cy - By) * (Dx - Bx)
    C = (Dx - Cx) * (Ay - Cy) - (Dy - Cy) * (Ax - Cx)
    D = (Ax - Dx) * (By - Dy) - (Ay - Dy) * (Bx - Dx)
    if A > 0 and B > 0 and C > 0 and D > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()