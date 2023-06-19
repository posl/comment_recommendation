def solve():
    ax,ay = map(int,input().split())
    bx,by = map(int,input().split())
    cx,cy = map(int,input().split())
    dx,dy = map(int,input().split())
    if (bx-ax)*(cy-ay)-(cx-ax)*(by-ay) > 0 and (cx-bx)*(dy-by)-(dx-bx)*(cy-by) > 0 and (dx-cx)*(ay-cy)-(ax-cx)*(dy-cy) > 0 and (ax-dx)*(by-dy)-(bx-dx)*(ay-dy) > 0:
        print("Yes")
    else:
        print("No")
solve()
