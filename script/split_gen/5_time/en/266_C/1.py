def main():
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    dx, dy = map(int, input().split())
    if (bx-ax)*(cy-by)-(cx-bx)*(by-ay) > 0 and (cx-bx)*(dy-cy)-(dx-cx)*(cy-by) > 0 and (dx-cx)*(ay-dy)-(ax-dx)*(dy-cy) > 0 and (ax-dx)*(by-ay)-(bx-ax)*(ay-dy) > 0:
        print('Yes')
    else:
        print('No')
