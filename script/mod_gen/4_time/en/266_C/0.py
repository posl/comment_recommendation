def main():
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    dx, dy = map(int, input().split())
    if ((dx - ax) * (by - ay) - (bx - ax) * (dy - ay) > 0) and ((dx - bx) * (cy - by) - (cx - bx) * (dy - by) > 0) and ((dx - cx) * (ay - cy) - (ax - cx) * (dy - cy) > 0) and ((dx - dx) * (ay - dy) - (ax - dx) * (dy - dy) > 0):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()