def main():
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    dx, dy = map(int, input().split())
    #print(ax, ay, bx, by, cx, cy, dx, dy)
    #print(bx-ax, by-ay, cx-bx, cy-by, dx-cx, dy-cy, ax-dx, ay-dy)
    #print(bx-ax, by-ay, cx-bx, cy-by, dx-cx, dy-cy, ax-dx, ay-dy)
    #print(bx-ax, by-ay, cx-bx, cy-by, dx-cx, dy-cy, ax-dx, ay-dy)
    if (bx-ax)*(cy-by) - (by-ay)*(cx-bx) > 0:
        if (cx-bx)*(dy-cy) - (cy-by)*(dx-cx) > 0:
            if (dx-cx)*(ay-dy) - (dy-cy)*(ax-dx) > 0:
                if (ax-dx)*(by-ay) - (ay-dy)*(bx-ax) > 0:
                    print("Yes")
                    return
    print("No")
    return
main()

if __name__ == '__main__':
    main()