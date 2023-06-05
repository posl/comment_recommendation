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

if __name__ == '__main__':
    main()