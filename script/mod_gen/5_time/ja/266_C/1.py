def main():
    ax,ay = map(int,input().split())
    bx,by = map(int,input().split())
    cx,cy = map(int,input().split())
    dx,dy = map(int,input().split())
    if ax == bx and ay == by:
        print('No')
        return
    if bx == cx and by == cy:
        print('No')
        return
    if cx == dx and cy == dy:
        print('No')
        return
    if dx == ax and dy == ay:
        print('No')
        return
    if ax == cx and ay == cy:
        print('No')
        return
    if bx == dx and by == dy:
        print('No')
        return
    if (ax - bx) * (cy - by) - (ay - by) * (cx - bx) > 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()